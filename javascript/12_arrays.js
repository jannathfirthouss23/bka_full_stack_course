const fruits = ["apple", "banana", "cherry"];
const numbers = [1, 2, 3, 4, 5];
const mixed = [1, "hello", true, null, { name: "Alice" }, [1, 2]];
const empty = [];

const arr1 = new Array(3); // [ <3 empty items> ]
const arr2 = Array.of(1, 2, 3); // [1, 2, 3]
const arr3 = Array.from("abc"); // ["a", "b", "c"]

// ACCESS & LENGTH

console.log(fruits[0]);
console.log(fruits[fruits.length - 1]);
console.log(fruits.at(-1));
console.log(fruits.length);

// UPDATE ELEMENTS

fruits[1] = "mango";
console.log(fruits);

// MUTATING METHODS (original array)

const nums = [1, 2, 3];

nums.push(4);
nums.pop();
nums.unshift(0); // add to start
nums.shift(); // remove from start

nums.splice(1, 1); // remove 1 item at index 1
nums.splice(1, 0, 99); // insert 99 at index 1
console.log(nums);

const arr = [3, 1, 4, 1, 5];
arr.reverse();
arr.sort();
arr.sort((a, b) => a - b);
arr.sort((a, b) => b - a);

// NON-MUTATING METHODS (return a new array)

const colors = ["red", "green", "blue"];

console.log(colors.slice(0, 2));
console.log(colors.concat(["yellow"]));
console.log([...colors, "pink"]);
console.log(colors.join("-"));
console.log(colors.includes("red"));
console.log(colors.indexOf("green"));
console.log(colors.indexOf("xyz"));

// HIGHER ORDER METHODS

const numList = [1, 2, 3, 4, 5];

numList.forEach((n) => console.log(n));
console.log(numList.map((n) => n * 2));
console.log(numList.filter((n) => n > 2));
console.log(numList.reduce((sum, n) => sum + n, 0));
console.log(numList.find((n) => n > 3));
console.log(numList.some((n) => n > 4));
console.log(numList.every((n) => n > 0));

// FLAT & FLATMAP

const nested = [1, [2, 3], [4, [5, 6]]];
console.log(nested.flat()); // [1,2,3,4,[5,6]] (1 level depth)
console.log(nested.flat(2)); // [1,2,3,4,5,6] (2 levels depth)
console.log(nested.flat(Infinity)); // fully flatten

console.log([1, 2, 3].flatMap((n) => [n, n * 2])); // [1,2,2,4,3,6]

// SPREAD OPERATOR

const a = [1, 2, 3];
const b = [4, 5, 6];

const copy = [...a]; // [1,2,3] (shallow copy)
const merged = [...a, ...b]; // [1,2,3,4,5,6]
console.log(copy);
console.log(merged);

// DESTRUCTURING

const [first, second, ...rest] = [10, 20, 30, 40, 50];
console.log(first);
console.log(second);
console.log(rest);

// Skip elements
const [, , third] = [10, 20, 30];
console.log(third);

// Default values
const [x = 1, y = 2] = [10];
console.log(x, y); // 10, 2

// CHECK IF SOMETHING IS AN ARRAY

console.log(Array.isArray([1, 2, 3]));
console.log(Array.isArray("hello"));

// NESTED ARRAYS (2D arrays / matrix)

const matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];

console.log(matrix[1][2]);

for (const row of matrix) {
    for (const cell of row) {
        console.log(cell);
    }
}