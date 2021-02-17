const checkBox = document.getElementById("toggle-btn");
const body = document.querySelector("body")

checkBox.addEventListener('click', () => {
    if (checkBox.checked === true ) {
        body.classList.remove('default');
        body.classList.add('light-theme');
    }else if (checkBox.checked === false ){
        body.classList.remove('light-theme');
        body.classList.add('default');
    }
});