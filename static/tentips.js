document.addEventListener('DOMContentLoaded', () => {

    // Change color theme of index page
    const colors = ['lightblue', 'lightpink', '#ffe8b6', '#97DDDA', 'lightgray'];
    let color_index = 0;
    
    document.querySelector('#change-color').addEventListener('click',  () => {
        document.querySelector('#homepage').style.backgroundColor = colors[color_index];        
        color_index = (color_index + 1) % colors.length;
        document.querySelector('#change-color').style.backgroundColor = colors[color_index]; 
    })
})

function yellow() {
    const favBtn = document.getElementById('addtofav');

    favBtn.classList.toggle('clicked');
    setTimeout(() => {
        favBtn.classList.toggle('yellow');
    }, 100);
    setTimeout(() => {
        favBtn.classList.toggle('clicked');
    }, 100)

}