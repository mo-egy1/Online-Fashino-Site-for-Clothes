// Navbar Menu
document.addEventListener("DOMContentLoaded", function() {
    let menuIcon = document.querySelector(".menu-icon");
    let navBar = document.querySelector(".main-navbar ul");
    let closeBtn = document.querySelector(".x-mark-icon");

    menuIcon.addEventListener("click", () => {
        navBar.classList.toggle("open");
    });

    closeBtn.addEventListener("click", () => {
        navBar.classList.remove("open");
    });

    document.addEventListener("click", function(event) {
        if (!navBar.contains(event.target) && !menuIcon.contains(event.target) && navBar.classList.contains("open")) {
            navBar.classList.remove("open");
        }
    });

    navBar.addEventListener("click", function(event) {
        event.stopPropagation();
    });
});

// Scroll To Top Button
let scrollToTopBtn = document.querySelector(".scrollToTop");

window.onscroll = function () {
    if (this.scrollY >= 220) {
        scrollToTopBtn.classList.add("showBtn");
    }
    else {
        scrollToTopBtn.classList.remove("showBtn");
    };
};

scrollToTopBtn.onclick = function () {
    window.scrollTo ({
        top: 0,
        behavior: "smooth",
    });
};