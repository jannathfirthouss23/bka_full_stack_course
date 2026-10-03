function greet() {
    console.log("Hello!");
}
greet();

function sayHi(name) {
    console.log("Hi, " + name);
}
sayHi("Alice");
sayHi("Bob");

function add(a, b) {
    return a + b;
}
const sum = add(5, 3);
console.log(sum);

const multiply = function (a, b) {
    return a * b;
};
console.log(multiply(4, 5));

const subtract = (a, b) => {
    return a - b;
};
console.log(subtract(10, 4));

const square = (x) => x * x;
console.log(square(5));

const double = x => x * 2;
console.log(double(7));

const sayHello = () => "Hello!";
console.log(sayHello());

function greetUser(name = "Guest") {
    console.log("Welcome, " + name);
}
greetUser();
greetUser("Alice");

// REST PARAMETERS

function sumAll(...numbers) {
    let total = 0;
    for (const n of numbers) {
        total += n;
    }
    return total;
}
console.log(sumAll(1, 2, 3, 4, 5));

// SPREAD OPERATOR

const nums = [1, 2, 3];
console.log(Math.max(...nums));

function getName() {
    return "Alice";
}
function welcome() {
    console.log("Welcome, " + getName());
}
welcome();

// IIFE - Immediately Invoked Function Expression

(function () {
    console.log("This runs immediately");
})();

(() => {
    console.log("Arrow IIFE also works");
})();

// INNER FUNCTION

function outerFn(name) {
    const message = "Hello";

    function innerFn() {
        console.log(message + ", " + name); // reads outer's name & message
    }

    innerFn();
}

outerFn("Alice");

function makeGreeter(greeting) {
    return function (name) {
        console.log(greeting + ", " + name);
    };
}

const hello = makeGreeter("Hello");
const hi = makeGreeter("Hi");

hello("Alice");
hi("Bob");

// CONSTRUCTOR FUNCTION - After OOPS

function Car(brand, model) {
    this.brand = brand;
    this.model = model;
    this.describe = function () {
        console.log(`${this.brand} ${this.model}`);
    };
}

const car1 = new Car("Toyota", "Camry");
const car2 = new Car("Honda", "Civic");

car1.describe();
car2.describe();