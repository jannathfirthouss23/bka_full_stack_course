// JS is single-threaded, but it handles async work (network, timers, etc.)
// without blocking the main thread, using the Event Loop.

// BASIC FETCH WITH .then()

fetch("https://jsonplaceholder.typicode.com/todos/1")
    .then((response) => response.json())
    .then((data) => console.log("Todo:", data))
    .catch((err) => console.log("Error:", err.message))
    .finally(() => console.log("Request finished"));

// CREATING OUR OWN PROMISE

const myPromise = new Promise((resolve, reject) => {
    const ok = true;
    if (ok) resolve("Success!");
    else reject("Failed!");
});

myPromise
    .then((value) => console.log(value))
    .catch((err) => console.log(err));

// RUN MULTIPLE IN PARALLEL WITH Promise.all([])

Promise.all([
    fetch("https://jsonplaceholder.typicode.com/todos/1").then((r) => r.json()),
    fetch("https://jsonplaceholder.typicode.com/todos/2").then((r) => r.json()),
    fetch("https://jsonplaceholder.typicode.com/todos/3").then((r) => r.json()),
])
    .then((todos) => console.log("All todos:", todos))
    .catch((err) => console.log("One failed:", err));

// Promise.all -> fails if ANY ONE rejects
// Promise.race -> first to response returns

// ASYNC / AWAIT

async function getTodo() {
    const response = await fetch("https://jsonplaceholder.typicode.com/todos/1");
    const data = await response.json();
    console.log("Todo:", data);
}
getTodo();

// EVENT LOOP

console.log("start");

setTimeout(() => console.log("macrotask"), 0);
Promise.resolve().then(() => console.log("microtask"));

console.log("end");