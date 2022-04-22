
// Hamburger menu
const hamburger = document.querySelector(".hamburger");
const navbar = document.querySelector(".navbar");

hamburger.addEventListener('click', () => {
    navbar.classList.toggle("active");
});

// Soundcloud Embed dropdown
const music_container = document.querySelector(".music_container");
const dropdown = document.querySelector("#dropdown");

dropdown.addEventListener('click', () => {
    music_container.classList.toggle("active");
});

// random color theme
$(function(){
    var themeClassName = "theme_"+Math.floor((Math.random() * 3) + 1);
    $('body').addClass(themeClassName);
});
