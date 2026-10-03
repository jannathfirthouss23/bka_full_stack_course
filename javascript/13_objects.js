const user = {
    name: "Alice",
    age: 25,
    isAdmin: true,
    hobbies: ["reading", "coding"],

    greet: function () {
        console.log("Hi, I am " + this.name);
    },

    introduce() {
        console.log(`I am ${this.name}, ${this.age} years old`);
    },

    // Arrow function - `this` will NOT refer to the object
    greetArrow: () => {
        console.log("Hi from " + this.name); // this.name is undefined
    },
};

// ACCESSING PROPERTIES

console.log(user.name);
console.log(user["age"]);
console.log(user.hobbies[0]);

// CALLING METHODS

user.greet();
user.introduce();
user.greetArrow();

// MODIFY PROPERTIES

user.email = "alice@mail.com";
user.age = 26;
delete user.isAdmin;
console.log(user);

// CHECK IF PROPERTY EXISTS

console.log("name" in user);
console.log("isAdmin" in user);
console.log(user.email !== undefined); // true

// LOOPING THROUGH AN OBJECT

// for...in loop - iterates over keys
for (const key in user) {
    console.log(key, "=", user[key]);
}

// Object.keys - returns array of keys
console.log(Object.keys(user));
Object.keys(user).forEach((key) => {
    console.log(key, ":", user[key]);
});

// Object.values - returns array of values
console.log(Object.values(user));
Object.values(user).forEach((val) => {
    console.log(val);
});

// Object.entries - returns array of [key, value] pairs
console.log(Object.entries(user));
for (const [key, value] of Object.entries(user)) {
    console.log(`${key} -> ${value}`);
}

// OBJECT WITH NESTED OBJECT AND FUNCTION

const car = {
    brand: "Toyota",
    model: "Camry",
    year: 2024,

    owner: {
        name: "Bob",
        age: 30,
    },

    start() {
        console.log(`${this.brand} ${this.model} is starting...`);
    },

    describe() {
        console.log(`${this.year} ${this.brand}, owned by ${this.owner.name}`);
    },
};

car.start();
car.describe();
console.log(car.owner.name);

// LOOP THROUGH NESTED OBJECT

for (const key in car) {
    if (typeof car[key] === "object" && car[key] !== null) {
        console.log(`${key}:`);
        for (const innerKey in car[key]) {
            console.log(`  ${innerKey} = ${car[key][innerKey]}`);
        }
    } else if (typeof car[key] !== "function") {
        console.log(`${key} = ${car[key]}`);
    }
}

// COPY & MERGE OBJECTS

const a = { x: 1, y: 2 };
const b = { y: 99, z: 3 };

const copy = { ...a }; // shallow copy = {x:1, y:2}
const merged = { ...a, ...b }; // merge = {x:1, y:99, z:3}
const merged2 = Object.assign({}, a, b); // same as above

console.log(copy);
console.log(merged);

// DESTRUCTURING

const { name, age, hobbies } = user;
console.log(name, age, hobbies);

// Rename while destructuring
const { name: userName, age: userAge } = user;
console.log(userName, userAge);

// Default values
const { city = "Unknown" } = user;
console.log(city);

// COMPUTED KEYS (dynamic key name)

const key = "score";
const player = {
    [key]: 100,
    [`${key}_max`]: 200,
};
console.log(player);

// FREEZE & SEAL (immutability)

const config = { theme: "dark", lang: "en" };

Object.freeze(config);
config.theme = "light"; // ignored or thrown error
console.log(config);

const settings = { volume: 50 };
Object.seal(settings); // cannot add or remove, but can modify existing
settings.volume = 80;
settings.brightness = 100; // ignored or thrown error
console.log(settings);