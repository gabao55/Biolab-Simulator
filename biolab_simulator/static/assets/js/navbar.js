let dropdown = document.querySelectorAll("nav ul li");
let mobileMenuIcon = document.querySelector('.close-menu-label');
let mobileMenu = document.querySelector("nav ul");
let mobileMenuItem = document.querySelectorAll("nav ul li.option");

function dropdownAnimationEntering() {
    let options;
    dropdown.forEach((item) => {
        item.addEventListener("mouseenter", () => {
            item.querySelector("i").classList.replace("down", "up");
            options = item.querySelector("ul");
            options.style.setProperty("visibility", "visible");
            options.style.setProperty("top", "70px");
            options.style.setProperty("visibility", "visible");
        })
    });
}

function dropdownAnimationLeaving() {
    let options;
    dropdown.forEach((item) => {
        item.addEventListener("mouseleave", () => {
            item.querySelector("i").classList.replace("up", "down");
            options = item.querySelector("ul");
            options.style.setProperty("visibility", "hidden");
            options.style.setProperty("top", "90px");
        })
    });
}

function dropdownAnimationClick() {
    mobileMenuItem.forEach((item) => {
        let arrowPosition;
        let options;
        item.addEventListener("mouseenter", () => {
            options = item.querySelector("ul");
            options.classList.toggle("invisible-item");
            arrowPosition = item.querySelector("i");
            arrowPosition.classList.replace("down", "up");
            options.style.setProperty("visibility", "visible");
            options.style.setProperty("top", "90px");
        });
        item.addEventListener("mouseleave", () => {
            options = item.querySelector("ul");
            options.classList.toggle("invisible-item");
            arrowPosition = item.querySelector("i");    
            arrowPosition.classList.replace("up", "down")
            options.style.setProperty("visibility", "hidden");
            options.style.setProperty("top", "70px");      
        })
    });
};

if(window.matchMedia("(min-width: 800px)").matches) {
    dropdownAnimationEntering();
    dropdownAnimationLeaving();
}

// Responsive navbar:
if (window.matchMedia("(max-width: 820px)").matches) {
    mobileMenuIcon.classList.toggle("invisible-item");
    mobileMenu.classList.add("mobile-menu", "invisible-item");
    let dropdownOption;
    mobileMenuItem.forEach((item) => {
        item.classList.add("mobile-menu-item");
        dropdownOption = item.querySelector("ul");
        if (dropdownOption) {
            dropdownOption.classList.toggle("invisible-item")
        }
    });
    dropdownAnimationClick();
}

mobileMenuIcon.addEventListener("click", () => {
    if (mobileMenuIcon.textContent === "≡") {
        mobileMenuIcon.textContent = "×";
        mobileMenu.classList.toggle("invisible-item");
    }
    else {
        mobileMenuIcon.textContent = "≡";
        mobileMenu.classList.toggle("invisible-item");
    }
});
