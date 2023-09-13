document.addEventListener('DOMContentLoaded', () => {
    const colors = ['lightblue', 'lightpink', '#ffe8b6', '#97DDDA', 'lightgray'];
    let color_index = 0;
    
    document.querySelector('#change-color').addEventListener('click',  () => {
        document.querySelector('#homepage').style.backgroundColor = colors[color_index];        
        color_index = (color_index + 1) % colors.length;
        document.querySelector('#change-color').style.backgroundColor = colors[color_index]; 
    })
})