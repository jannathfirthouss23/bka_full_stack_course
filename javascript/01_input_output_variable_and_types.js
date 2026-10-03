// OUTPUT

console.log("Hello World");
console.warn("This is a warning");
console.error("This is an error");
console.info("This is info")
console.table([{ name: "Alice", age: 25 }]);
// console.clear();

// INPUT (browser only)

alert("Hello!");
let isOk = confirm("Are you sure?");
console.log(isOk);

let userName = prompt("Enter your name");
console.log(userName);

// VARIABLES

var oldStyle = "function-scoped, avoid using";
let age = 25;
const PI = 3.14;

age = 26;
// PI = 3.14159; Error, cannot reassign const

// ARRAY EXAMPLE

const fruits = ["apple", "banana", "cherry"];
console.log(fruits);
console.log(fruits[0]);

// OBJECT EXAMPLE

const person = { name: "Alice", age: 25, city: "Paris" };
console.log(person);
console.log(person.name);

// DATA TYPES

console.log(typeof "James");
console.log(typeof 42);
console.log(typeof 42n);
console.log(typeof true);
console.log(typeof undefined);
console.log(typeof null); // null are objects too
console.log(typeof Symbol("id")); // symbol (unique value)
console.log(typeof {});
console.log(typeof []); // arrays are objects too

// TYPE CONVERSION

console.log(Number("42"));
console.log(String(42));
console.log(Boolean(0));
console.log(Boolean(1));

console.log(parseInt("42px")); // 42
console.log(parseFloat("3.14kg")); // 3.14

// TEMPLATE LITERALS

let name = "Alice";
console.log(`Hello, ${name}!`);
console.log(`Sum is ${2 + 3}`);
