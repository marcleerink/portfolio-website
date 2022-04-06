// Soundcloud Embed dropdown

const scWrapper = document.querySelector("#sc-wrapper");
const dropdown = document.querySelector("#dropdown");

dropdown.onclick = function() {
    if (scWrapper.style.display === "none") {
        scWrapper.style.display = "flex";
        dropdown.innerHTML = "<i class='fa-solid fa-minus'></i>"
    } else {
        scWrapper.style.display = "none";
        dropdown.innerHTML = "<i class='fa-solid fa-caret-down'>"
    }
};

