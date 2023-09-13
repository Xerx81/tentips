.open "C:/Users/OM KANWAR/Documents/VS Code/CS50x Final Project/tentips/tentips.db"

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    description TEXT NOT NULL,
    image TEXT NOT NULL,
    tips TEXT NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY(category_id) REFERENCES categories(id)
);

CREATE TABLE favorites (
    book_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE,
    FOREIGN key(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL
);

INSERT INTO categories (category) VALUES ('finance');
INSERT INTO books (title, author, description, image, tips, category_id) VALUES ('The Self Taught Programmer', 'Cory Althoff', 'This book teaches how to be a software developer without a degree by self teaching.', 'https://m.media-amazon.com/images/I/41Jl2Tn2HjL.jpg', 'Start with the Fundamentals: Begin with the basics of programming languages and concepts like variables, loops, and functions. Understanding the fundamentals lays a strong foundation for your future learning.#Practice Regularly: Consistency is key to becoming a proficient programmer. Set aside dedicated time each day to practice coding and work on projects that challenge you.#Build Real Projects: Instead of just reading or following tutorials, work on real-world projects. This hands-on approach helps you apply what you've learned and solidify your skills.#Join Coding Communities: Engage with online coding communities and forums to seek help, share knowledge, and collaborate with others. Active participation in these communities can lead to valuable insights and support.#Read Other People's Code: Analyzing and understanding code written by others is a crucial skill. It exposes you to different coding styles, techniques, and problem-solving approaches.#Don't Fear Mistakes: Mistakes are a natural part of the learning process. Embrace them as opportunities to learn and grow. Debugging and troubleshooting are valuable skills for any programmer.#Learn Data Structures and Algorithms: Understanding data structures and algorithms is essential for writing efficient and optimized code. Take the time to study common data structures and algorithms.#Document Your Learning: Keep track of your progress and notes as you learn. Creating documentation helps reinforce your knowledge and allows you to review concepts easily in the future.#Seek Feedback: Share your projects and code with others to receive feedback. Constructive criticism can help you identify areas for improvement and gain valuable insights from more experienced programmers.#Stay Curious and Open-Minded: The world of programming is vast and ever-changing. Stay curious and open to new technologies and languages. Continuously learning and adapting is essential for long-term success as a programmer.', 1);

Start with the Fundamentals: Begin with the basics of programming languages and concepts like variables, loops, and functions. Understanding the fundamentals lays a strong foundation for your future learning.#Practice Regularly: Consistency is key to becoming a proficient programmer. Set aside dedicated time each day to practice coding and work on projects that challenge you.#Build Real Projects: Instead of just reading or following tutorials, work on real-world projects. This hands-on approach helps you apply what you've learned and solidify your skills.#Join Coding Communities: Engage with online coding communities and forums to seek help, share knowledge, and collaborate with others. Active participation in these communities can lead to valuable insights and support.#Read Other People's Code: Analyzing and understanding code written by others is a crucial skill. It exposes you to different coding styles, techniques, and problem-solving approaches.#Don't Fear Mistakes: Mistakes are a natural part of the learning process. Embrace them as opportunities to learn and grow. Debugging and troubleshooting are valuable skills for any programmer.#Learn Data Structures and Algorithms: Understanding data structures and algorithms is essential for writing efficient and optimized code. Take the time to study common data structures and algorithms.#Document Your Learning: Keep track of your progress and notes as you learn. Creating documentation helps reinforce your knowledge and allows you to review concepts easily in the future.#Seek Feedback: Share your projects and code with others to receive feedback. Constructive criticism can help you identify areas for improvement and gain valuable insights from more experienced programmers.#Stay Curious and Open-Minded: The world of programming is vast and ever-changing. Stay curious and open to new technologies and languages. Continuously learning and adapting is essential for long-term success as a programmer.