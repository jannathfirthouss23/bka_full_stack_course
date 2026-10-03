// String Operations

const single = 'Hello';
const double = "World";
const backtick = `Hi there`;

// LENGTH & ACCESS

const str = "Hello JavaScript";

console.log(str.length);
console.log(str[0]);
console.log(str[str.length - 1]);
console.log(str.charAt(1));
console.log(str.at(-1));

// CASE METHODS

console.log(str.toUpperCase());
console.log(str.toLowerCase());

// SEARCH METHODS

console.log(str.indexOf("Java"));
console.log(str.indexOf("xyz"));
console.log(str.lastIndexOf("a"));
console.log(str.includes("Script"));
console.log(str.startsWith("Hello"));
console.log(str.endsWith("Script"));

// EXTRACT METHODS

console.log(str.slice(6, 10));
console.log(str.slice(-6));
console.log(str.substring(0, 5));

// MODIFY METHODS

console.log(str.replace("Hello", "Hi"));
console.log("aaa".replaceAll("a", "b"));
console.log("  spaced  ".trim());
console.log("  spaced  ".trimStart());
console.log("  spaced  ".trimEnd());

console.log("ab".repeat(3));
console.log("5".padStart(3, "0"));
console.log("5".padEnd(3, "0"));

// SPLIT & JOIN

console.log("a,b,c".split(","));
console.log("hello".split(""));
console.log(["a", "b", "c"].join("-"));

// CONCATENATION

console.log("Hello" + " " + "World");
console.log("Hello".concat(" ", "World"));

// TEMPLATE LITERALS (backticks)

const name = "Alice";
const age = 25;

console.log(`Hello, ${name}!`);
console.log(`Sum = ${2 + 3}`);
console.log(`${name} is ${age} years old`);

// Multi-line strings
console.log(`This is
a multi-line
string`);

// ESCAPE CHARACTERS

console.log("She said \"hi\"");
console.log('It\'s fine');
console.log("Line 1\nLine 2");
console.log("Col1\tCol2");
console.log("Back\\slash");

// COMPARISON

console.log("apple" === "apple");
console.log("apple" < "banana");
console.log("A" < "a");

// CONVERT OTHER TYPES TO STRING

console.log(String(123));
console.log((123).toString());
console.log(String(true));
console.log(String(null));