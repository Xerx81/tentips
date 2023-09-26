document.addEventListener('DOMContentLoaded', () => {
    
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