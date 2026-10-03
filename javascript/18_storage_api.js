// LOCAL STORAGE

localStorage.setItem("name", "Alice");
console.log(localStorage.getItem("name"));

localStorage.removeItem("name");
console.log(localStorage.getItem("name"));

console.log(localStorage.length);
console.log(localStorage.key(0));

// localStorage.clear();

// SESSION STORAGE - cleared when tab is closed

sessionStorage.setItem("token", "abc123");
console.log(sessionStorage.getItem("token"));

// STORING OBJECTS (must convert to JSON, storage only stores strings)

const user = { name: "Alice", age: 25 };

localStorage.setItem("user", JSON.stringify(user));
const saved = JSON.parse(localStorage.getItem("user"));

console.log(saved);
console.log(saved.name);

// COOKIES

document.cookie = "theme=dark; max-age=3600; path=/";
console.log(document.cookie);