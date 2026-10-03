// SELECTORS

const title = document.getElementById("title");
console.log(title);

const boxes = document.getElementsByClassName("box");
console.log(boxes);

const inputs = document.getElementsByTagName("input");
console.log(inputs);

const firstBox = document.querySelector(".box");
console.log(firstBox);

const allBoxes = document.querySelectorAll(".box");
console.log(allBoxes);

const inputByName = document.getElementsByName("username");
console.log(inputByName);

// EVENT LISTENER (after DOM is fully loaded)

document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("myBtn");

    btn.addEventListener("click", () => {
        btn.style.backgroundColor = "tomato";
        btn.style.color = "white";
    });
});