// Prototype: A separate object in memory that holds shared methods.

// CONSTRUCTOR FUNCTION EXAMPLE - It is the older pattern from before ES6 (2015)

function MyFunctionArray() {
    this.items = [];
    this.length = 0;
}

MyFunctionArray.prototype.push = function (item) {
    this.items[this.length] = item;
    this.length++;
};

MyFunctionArray.prototype.pop = function () {
    this.length--;
    const removed = this.items[this.length];
    this.items.length = this.length;
    return removed;
};

const list3 = new MyFunctionArray();
const list4 = new MyFunctionArray();

list3.push("apple");
list3.push("banana");
list4.push("cherry");

console.log(list3.length, list4.length);
console.log(list3.push === list4.push); // Same methods, only different instance (memory address)
console.log(list3.push === MyFunctionArray.prototype.push); // push is same function reference (memory address)

// CLASS EXAMPLE - Modern Prototype Usage

class MyClassArray {
    constructor() {
        this.items = [];
        this.length = 0;
    }

    push(item) {
        this.items[this.length] = item;
        this.length++;
    }

    pop() {
        this.length--;
        return this.items[this.length];
    }
}

const list1 = new MyClassArray();
const list2 = new MyClassArray();

list1.push("apple");
list1.push("banana");
list2.push("cherry");

console.log(list1.length, list2.length);
console.log(list1.push === list2.push); // both instances share the same push from prototype
console.log(list1.push === MyClassArray.prototype.push); // push is same function reference

// BUILT-IN Data Structures uses still Prototypes

console.log(typeof Array, typeof Object, typeof String);
// type "function" <- still a function, not a class
// `Array`, `Object`, `String` etc. are all still constructor functions internally.
// They use `.prototype` the same way they did in 1995.

/** IN-BUILT PROTOTYPES - basically returns the top parent prototype in the chain */

// PROTOTYPE CHAIN - Get the parent prototype (parent class)

const arr = [];
console.log(Object.getPrototypeOf(arr));

const obj = {};
console.log(Object.getPrototypeOf(obj));

class Animal {}
class Dog extends Animal {}
const d = new Dog();
console.log(Object.getPrototypeOf(d)); // Dog.Prototype parent = Animal.Prototype
console.log(Object.getPrototypeOf(Dog.prototype) === Animal.prototype);

// CREATE AN OBJECT WITH A CUSTOM PROTOTYPE

const parent = { greet() { console.log("hi"); } };
const child = Object.create(parent);
console.log(Object.getPrototypeOf(child)); // { greet: [Function: greet] }
console.log(Object.getPrototypeOf(child) === parent);

// CHECK OWN vs INHERITED PROPERTY

const user = { name: "Bob" };

console.log(user.hasOwnProperty("name"));
console.log(user.hasOwnProperty("toString")); // false
