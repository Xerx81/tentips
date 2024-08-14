document.addEventListener('DOMContentLoaded', () => {
    
    // Responsive navbar
    const toggle_btn = document.getElementsByClassName('toggle-nav')[0];
    const items = document.getElementsByClassName('items')[0];
    const search_bar = document.getElementsByClassName('search-bar')[0];

    toggle_btn.addEventListener('click', () => {
        items.classList.toggle('active');
        search_bar.classList.toggle('active');
    })

    // Search button
    const search_inp = document.querySelector('#search');
    const search_btn = document.querySelector('#search-btn');
    
    search_btn.disabled = true;

    search_inp.onkeyup = () => {
        if (search_inp.value.length > 0 && search_inp.value !== " ") {
            search_btn.disabled = false;
            search_btn.classList.add('search-btn');
        }
        else {
            search_btn.disabled = true;
            search_btn.classList.remove('search-btn');
        }
    }

    if (document.title === 'Home') {

        // Change color theme of index page
        const colors = ['lightblue', 'lightpink', '#ffe8b6', '#97DDDA', 'lightgray'];
        let color_index = 0;
        
        document.querySelector('#change-color').addEventListener('click',  () => {
            document.querySelector('#homepage').style.backgroundColor = colors[color_index];        
            color_index = (color_index + 1) % colors.length;
            document.querySelector('#change-color').style.backgroundColor = colors[color_index]; 
        });
    }
    
    const remFavBtns = document.querySelectorAll('.rem-fav');

    // Add a click event listener to each "rem-fav" button
    remFavBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove the clicked button
            btn.parentElement.style.animationPlayState = 'running';
            btn.parentElement.addEventListener('animationend', () => {
                btn.parentElement.remove();
                location.reload();
            });
        });
    });
})

function favorite(id) {
    const favBtn = document.getElementById('addtofav');

    favBtn.classList.toggle('clicked');
    setTimeout(() => {
        favBtn.classList.toggle('yellow');
    }, 100);
    setTimeout(() => {
        favBtn.classList.toggle('clicked');
    }, 100)

    fetch(`/add/${id}`)
    .then(response => response.json())
    .then(result => console.log(result))
}

function rem_fav(id) {
    fetch(`/add/${id}`)
    .then(response => response.json())
    .then(result => console.log(result))
}

function showPass() {
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    }
    else {
        x.type = "password";
    }
}