// CALLBACK - a function passed as an argument to another function

function greet(name, callback) {
    console.log("Hello " + name);
    callback();
}

function sayBye() {
    console.log("Bye!");
}

greet("Alice", sayBye);
// Hello Alice
// Bye!

// CALLBACK WITH ARROW FUNCTION

greet("Bob", () => {
    console.log("See you later!");
});

// HIGHER ORDER FUNCTION (HOF) - a function that takes a function OR returns a function

function multiplier(factor) {
    return function (x) {
        return x * factor;
    };
}

const double = multiplier(2);
const triple = multiplier(3);

console.log(double(5));
console.log(triple(5));

// ARRAY HIGHER ORDER METHODS

const nums = [1, 2, 3, 4, 5];

nums.forEach((n) => console.log(n));

const doubled = nums.map((n) => n * 2);
console.log(doubled);

const evens = nums.filter((n) => n % 2 === 0);
console.log(evens); // [2, 4]

const total = nums.reduce((sum, n) => sum + n, 0);
console.log(total);

const firstBig = nums.find((n) => n > 3);
console.log(firstBig);

// findIndex - returns the index of first matching element
const idx = nums.findIndex((n) => n > 3);
console.log(idx); // 3

// some - true if at least one element passes
console.log(nums.some((n) => n > 4)); // true

// every - true if all elements pass
console.log(nums.every((n) => n > 0)); // true

console.log([3, 1, 5, 2].sort((a, b) => a - b)); // ascending
console.log([3, 1, 5, 2].sort((a, b) => b - a)); // descending

// CHAINING HOFs

const result = [1, 2, 3, 4, 5]
    .filter((n) => n % 2 === 1)
    .map((n) => n * 10)
    .reduce((a, b) => a + b);

console.log(result);

/** CALLBACK HELL
    fetchUser(id, (user) => {
        fetchPosts(user, (posts) => {
            fetchComments(posts[0], (comments) => {
                console.log(comments); // nested functions
            });
        });
    });
 **/