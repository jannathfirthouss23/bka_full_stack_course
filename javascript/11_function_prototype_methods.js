// Function Prototype Methods (call, apply, bind)

// Every function in JS has 3 built-in methods: call, apply, bind
// it will let us control what `this` refers to when calling function.

const person = { name: "Alice" };

function sayHi() {
    console.log("Hi, " + this.name);
}

// sayHi(); // "Hi, undefined"

/** CALL */

sayHi.call(person); // Pass with arguments

function greet(greeting, punctuation) {
    console.log(`${greeting}, ${this.name}${punctuation}`);
}

greet.call(person, "Hello", "!"); // Pass with arguments along with function arguments

/** APPLY - same as call, but arguments are passed as an array */

greet.apply(person, ["Hi", "."]);

const args = ["Hey", "?"];
greet.apply(person, args);

/** BIND - returns a NEW function with `this` permanently bound */

const greetAlice = greet.bind(person, "Hello");
greetAlice("!"); // 1st time called
greetAlice("?"); // 2nd time called

/** BORROWING METHODS from one object to use on another */

const user1 = {
    name: "Alice",
    introduce: function () {
        console.log("I am " + this.name);
    },
};

const user2 = { name: "Bob" };

user1.introduce.call(user2);

// PARTIAL APPLICATION using bind (preset some arguments)

function multiply(a, b) {
    return a * b;
}

const double = multiply.bind(null, 2); // `this` is not used so null is passed
console.log(double(5));
console.log(double(10));

const triple = multiply.bind(null, 3); // `this` is not used so null is passed
console.log(triple(5));

/** ARROW FUNCTIONS - Arrow functions don't have their own `this` */

const arrow = () => {
    console.log(this);
};

arrow.call({ name: "X" });