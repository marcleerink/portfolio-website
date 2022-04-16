// Hamburger menu
const hamburger = document.querySelector(".hamburger");
const navbar = document.querySelector(".navbar");

hamburger.addEventListener('click', () => {
    navbar.classList.toggle("active");
});

// Soundcloud Embed dropdown
const scWrapper = document.querySelector("#sc-wrapper");
const dropdown = document.querySelector("#dropdown");

dropdown.addEventListener('click', () => {
    scWrapper.classList.toggle("active");
});

