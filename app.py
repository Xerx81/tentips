import sqlite3

from flask import Flask, jsonify, redirect, render_template, request, session
from flask_session import Session
from random import choice
from werkzeug.security import check_password_hash, generate_password_hash

from myfunc import login_required


# Configure application
app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = 0
    return response


@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    with sqlite3.connect("tentips.db") as con:
        db = con.cursor()

        
        books = db.execute("SELECT * FROM books ORDER BY id DESC")
        books = books.fetchall()

        # for book in books
        # book[0] = id, 
        # book[1] = title, 
        # book[2] = author, 
        # book[3] = description, 
        # book[4] = image,
        # book[5] = tips 
        # book[6] = category_id

        categories = db.execute("SELECT * FROM categories")
        categories = categories.fetchall()

        # Random tip
        rand_book = choice(books)
        rand_title = rand_book[1]
        rand_tip = choice(rand_book[5].split('#'))
        rand_tip = rand_tip.split(':')

        # Search
        if request.method == 'POST':

            searched_title = request.form.get('search')
            searched_title_cap = searched_title.title()
                    
            # Use '%' to match any characters before and after the search term
            search_query = f"%{searched_title_cap}%"

            # Execute the SQL query to search for titles and fetch them
            search_results = db.execute("SELECT * FROM books WHERE title LIKE ?", (search_query, ))
            search_results = search_results.fetchall()
            # not_found = ""
            # if not search_results:
            #     not_found = "Book not found"

            return render_template("index.html",
                search_results=search_results,
                # not_found=not_found,
                searched_title=searched_title
            )

        return render_template("index.html",
            books=books,
            categories=categories,
            rand_tip = rand_tip,
            rand_title=rand_title,
        )   


@app.route("/search", methods=["GET", "POST"])
def search():
    with sqlite3.connect("tentips.db") as con:
        db = con.cursor()

        # Search
        if request.method == 'POST':

            searched_title_cap = request.form.get('search')
            searched_title_cap = searched_title_cap.title()
                    
            # Use '%' to match any characters before and after the search term
            search_query = f"%{searched_title_cap}%"

            # Execute the SQL query to search for titles and fetch them
            search_results = db.execute("SELECT title FROM books WHERE title LIKE ?", (search_query, ))
            search_results = search_results.fetchall()
            if not search_results:
                search_results = "Book not found"

            return search_results


@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    with sqlite3.connect("tentips.db") as con:
        db = con.cursor()

        # Show this page to admin only
        admin_username = "Xerx"
        admin_id = db.execute("SELECT id FROM users WHERE username = ?", [admin_username])
        admin_id = admin_id.fetchone()

        if session["id"] != admin_id[0]:
            return "not allowed"

        if request.method == "POST":
            title = request.form.get("title")
            title = title.title()

            author = request.form.get("author")
            author = author.title()

            description = request.form.get("description")
            image = request.form.get("image")
            tips = request.form.get("tips")

            
            category = request.form.get("new_category")
            if category:
                # Check if category already exists
                c = db.execute("SELECT category FROM categories WHERE category = ?", [category])
                c = c.fetchone()
                if c:
                    return "Category already exist"
                
                # Insert new category into databse
                db.execute("INSERT INTO categories (category) VALUES (?)", (category,))
                con.commit()

                # Fetch id of new category
                category_id = db.execute("SELECT id FROM categories WHERE category = ?", [category])
                category_id = category_id.fetchone()[0]
            else:
                category = request.form.get("category")
                category_id = db.execute("SELECT id FROM categories WHERE category = ?", [category])
                category_id = category_id.fetchone()[0]

            # Check if book title already exists
            book = db.execute("SELECT * FROM books WHERE title = ?", [title])
            book = book.fetchall()

            if len(book) < 1:
                db.execute("INSERT INTO books (title, author, description, image, tips, category_id) VALUES (?, ?, ?, ?, ?, ?)", (title, author, description, image, tips, category_id))
                con.commit()

            return redirect("/")
        else:
            categories = db.execute("SELECT category FROM categories")
            categories = categories.fetchall()

            return render_template("admin.html",
                categories=categories
            )


@app.route("/tips/<int:book_id>")
def tips(book_id):
    with sqlite3.connect("tentips.db") as con:
        db = con.cursor()

        # Get the book of given id
        book = db.execute("SELECT * FROM books WHERE id = ?", [book_id])
        book = book.fetchone()

        # Get the books with the same category as above book
        sim_books = db.execute("SELECT * FROM books WHERE category_id = ?", [book[6]])
        sim_books = sim_books.fetchall()

        # Get books from favorites table for current user
        user_id = session["id"]
        try:
            fav_book = db.execute("SELECT * FROM favorites WHERE book_id = ? AND user_id = ?", (book_id, user_id)) 
            fav_book = fav_book.fetchall()
        except:
            fav_book = []

        return render_template("tips.html",
            book=book,
            sim_books=sim_books,
            fav_book = fav_book
        )


@app.route("/favorites")
def favorites():
    with sqlite3.connect("tentips.db") as con:
        db = con.cursor ()

        # Get books from favorites table for current user
        user_id = session["id"]
        fav_books = db.execute("SELECT * FROM favorites JOIN books ON book_id=books.id JOIN categories ON category_id = categories.id WHERE user_id= ? ORDER BY title", [user_id]) 
        fav_books = fav_books.fetchall()

        return render_template(
            "favorites.html",
            fav_books = fav_books
        )

@app.route("/add/<int:book_id>")
def addtofav(book_id):
    with sqlite3.connect("tentips.db") as con:
        db = con.cursor ()

        user_id = session["id"]

        fav_books = db.execute("SELECT * FROM favorites WHERE user_id= ? AND book_id = ?", (user_id, book_id)) 
        fav_books = fav_books.fetchall()

        if fav_books:

            # Remove from favorites
            db.execute("DELETE FROM favorites WHERE user_id = ? AND book_id = ?", (user_id, book_id))
            return jsonify({'message': 'Removed from favorites'})
        
        # Add to favorites
        db.execute("INSERT INTO favorites (book_id, user_id) VALUES (?, ?)", (book_id, user_id))
        con.commit()
        return jsonify({'message': 'Added to favorites'})


@app.route("/settings", methods=["GET", "POST"])
def settings():
    with sqlite3.connect("tentips.db") as con:
        db = con.cursor()
        
        # Fetch info of current user from db 
        user_id = session["id"]
        user_info = db.execute("SELECT * FROM users WHERE id = ?", (user_id, ))
        user_info = user_info.fetchone()

        if request.method == "POST":
            new_username = request.form.get("new_username")
            old_password = request.form.get("old_password")
            new_password = request.form.get("new_password")
            confirm_password = request.form.get("confirm_password")

            if new_username:
            
                # Ensure that username is of appropriate length
                if len(new_username) < 3:
                    return render_template("settings.html",
                        user_info=user_info,
                        u_len="enter altleast 3 characters"
                    )
                
                # Check if username is already taken
                usernames = db.execute("SELECT username FROM users")
                usernames = usernames.fetchall()
                if usernames:
                    for username in usernames:
                        if new_username == username[0]:
                            return render_template("settings.html",
                                user_info=user_info,
                                taken="username already taken!",
                            )
                        
                # Update the username in databasse
                db.execute("UPDATE users SET username = ? WHERE id = ?", (new_username, user_info[0]))
                return redirect("/settings")
            
            elif old_password:
                hash = db.execute("SELECT hash FROM users WHERE id = ?", (user_info[0], ))
                hash = hash.fetchone()

                if not check_password_hash(hash[0], old_password):
                    return render_template("settings.html", 
                        user_info=user_info,
                        error="Invalid password",
                    )
                
                if len(new_password) < 8:
                    return render_template("settings.html",
                        user_info=user_info,
                        p_len="enter atleast 8 characters!"
                    )
                
                if new_password == old_password:
                    return render_template("settings.html",
                        user_info=user_info,
                        p_len="Cannot use the same password!"
                    )
                
                # Check if password match in both fields
                if new_password != confirm_password:
                    return render_template("settings.html",
                        user_info=user_info,
                        match="password do not match!"
                    )  
                
                # Generate hash code of password and save in sql database
                new_hash = generate_password_hash(new_password)
                db.execute("UPDATE users SET hash = ? WHERE id = ?", (new_hash, user_info[0]))

                return render_template("settings.html",
                    user_info=user_info,
                    changed="Password changed successfully"
                )
            
        return render_template("settings.html",
            user_info=user_info,
        )       


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # Setup connection with sql database
        with sqlite3.connect("tentips.db") as con:
            db = con.cursor()

            username = request.form.get("username")
            password = request.form.get("password")
            confirmation = request.form.get("confirmation")

            # Ensure that username is of appropriate length
            if len(username) < 3:
                return render_template("register.html", u_len="enter altleast 3 characters")
            
            # Check if username is already taken
            usernames = db.execute("SELECT username FROM users")
            usernames = usernames.fetchall()
            if usernames:
                for u in usernames:
                    if username == u[0]:
                        return render_template("register.html", taken="username already taken!")
                
            # Ensure the password is of appropriate length    
            if len(password) < 8:
                return render_template("register.html", p_len="enter atleast 8 characters!")
            
            # Check if password match in both fields
            if password != confirmation:
                return render_template("register.html", match="password do not match!")  
            
            # Generate hash code of password and save in sql database
            hash = generate_password_hash(password)
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (username, hash))
            con.commit()

            # Log user in
            id = db.execute("SELECT id FROM users WHERE username = ?", [username])
            id = id.fetchone()
            print(id)
            session["id"] = id[0]
            
            return redirect("/")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Clear previous session
    session.clear()

    if request.method == "POST":
        # Connect sql database
        with sqlite3.connect("tentips.db") as con:
            db = con.cursor()

            username = request.form.get("username")
            password = request.form.get("password")

            # Check if username and password are correct
            try:
                temp = db.execute("SELECT * FROM users WHERE username = ?", [username])
                temp = temp.fetchall()

                if not check_password_hash(temp[0][2], password):
                    return render_template("login.html", error="Invalid username and/or password")
                
                # Log user in
                session["id"] = temp[0][0]

                # Redirect to home page
                return redirect("/")
                
            except:
                return render_template("login.html", error="Invalid username and/or password")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

