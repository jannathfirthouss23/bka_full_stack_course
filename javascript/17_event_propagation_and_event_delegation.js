/** EVENT PROPAGATION - how events travel through the DOM

An event passes through 2 phases:
    1. CAPTURING - runs before the actual target
    3. BUBBLING  - back UP from target to window  (target to parent, default phase)
*/

const grandparent = document.getElementById("grandparent");
const parent = document.getElementById("parent");
const child = document.getElementById("child");

// BUBBLING (target to parent)
// grandparent.addEventListener("click", () => console.log("grandparent clicked"));
parent.addEventListener("click", () => console.log("parent clicked"));
child.addEventListener("click", () => console.log("child clicked"));

// CAPTURING - Runs before the actual target
grandparent.addEventListener("click",
() => console.log("grandparent (capture)"),
{ capture: true });

// STOP PROPAGATION & PREVENT DEFAULT
const box = document.getElementById("box");
const link = document.getElementById("link");

box.addEventListener("click", () => console.log("box clicked"));

link.addEventListener("click", (e) => {
    e.stopPropagation(); // stops bubble up to box except CAPTURING events
    e.preventDefault(); // stops browser from going to google.com
});

/** EVENT DELEGATION - one listener on the parent handles events from many children */

const list = document.getElementById("list");

list.addEventListener("click", (e) => {
    if (e.target.tagName === "LI") {
        console.log("Clicked:", e.target.textContent);
    }
});
