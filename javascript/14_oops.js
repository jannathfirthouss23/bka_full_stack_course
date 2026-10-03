class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    greet() {
        console.log(`Hi, I am ${this.name}`);
    }
}

const p1 = new Person("Alice", 25);
const p2 = new Person("Bob", 30);

p1.greet();
p2.greet();

console.log(p1.name);

// INHERITANCE - extends & super

class Employee extends Person {
    constructor(name, age, role) {
        super(name, age); // calls parent constructor
        this.role = role;
    }

    describe() {
        console.log(`${this.name} works as ${this.role}`);
    }
}

const emp = new Employee("Charlie", 28, "Developer");
emp.greet();
emp.describe();

// ENCAPSULATION - private fields with #

class Account {
    #balance = 0; // private, only accessible inside the class

    deposit(amount) {
        this.#balance += amount;
    }

    showBalance() {
        console.log(`Balance: ${this.#balance}`);
    }
}

const acc = new Account();
acc.deposit(500);
acc.showBalance();
// console.log(acc.#balance); Error - private field

// POLYMORPHISM - same method, different behavior

class Animal {
    speak() {
        console.log("Some sound");
    }
}

class Dog extends Animal {
    speak() {
        console.log("Woof!");
    }
}

class Cat extends Animal {
    speak() {
        console.log("Meow!");
    }
}

const animals = [new Dog(), new Cat(), new Animal()];
animals.forEach((a) => a.speak()); // Woof! Meow! Some sound

// STATIC MEMBERS - belong to the class, not to instances

class MathHelper {
    static PI = 3.14159;

    static area(r) {
        return MathHelper.PI * r * r;
    }
}

console.log(MathHelper.PI); // 3.14159
console.log(MathHelper.area(5)); // 78.53975

// `this` keyword

console.log(this); // window (in browser, at top level)

// INSIDE AN OBJECT METHOD - `this` refers to the object

const car = {
    brand: "Toyota",
    showBrand() {
        console.log(this.brand);
    },
};
car.showBrand();

// INSIDE A CLASS - `this` refers to the instance

class Dog2 {
    constructor(name) {
        this.name = name;
    }
    bark() {
        console.log(`${this.name} says Woof!`);
    }
}
new Dog2("Rex").bark();

// INSIDE AN ARROW FUNCTION

const obj = {
    name: "Alice",
    regular: function () {
        console.log(this.name); // this works
    },
    arrow: () => {
        console.log(this.name); // `this` not works in arrow function
    },
};
obj.regular();
obj.arrow();

// CALLBACK PITFALL - `this` is lost in regular callbacks

const user = {
    name: "Bob",
    greetLater() {
        // setTimeout calls this as a plain function (no owner)
        setTimeout(function () {
            console.log("Hi, " + this.name); // Hi, undefined
        }, 100);

        // setTimeout calls this as arrow function with owner
        setTimeout(() => {
            console.log("Hi, " + this.name); // Hi, Bob
        }, 200);
    },
};
user.greetLater();
