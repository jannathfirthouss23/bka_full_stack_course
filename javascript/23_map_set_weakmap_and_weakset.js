// MAP - key value pairs (like Object, but keys can be ANY type (object, function, number)
// preserves insertion order & has .size()

const userScores = new Map();

userScores.set("alice", 100);
userScores.set("bob", 85);
userScores.set(1, "first");
userScores.set(true, "yes");

let obj = { id: 1 };
userScores.set(obj, "object as key!");

console.log(userScores.get("alice"));
console.log(userScores.get(obj));
console.log(userScores.has("bob"));
console.log(userScores.size);

userScores.delete("bob");
console.log(userScores.size);

obj = null // unlike WeakMap the obj even if reference is null, still have the key-value pair.

for (const [key, value] of userScores) {
    console.log(key, "->", value);
}

userScores.forEach((value, key) => {
    console.log(key, "=", value);
});

console.log([...userScores.keys()]);
console.log([...userScores.values()]);

// userScores.clear();

// SET - collection of UNIQUE values compare by reference, not content.

const fruits = new Set();

fruits.add("cherry");
fruits.add("apple");
fruits.add("banana");
fruits.add("apple");

console.log(fruits.size);
console.log(fruits.has("apple"));
console.log(fruits.has("mango"));

fruits.delete("banana");
console.log(fruits.size);

for (const fruit of fruits) {
    console.log(fruit);
}

const nums = [1, 2, 2, 3, 4, 4, 5];
const unique = [...new Set(nums)];
console.log(unique);

// fruits.clear();

// WEAK MAP - Map with weak references

/**
    Keys MUST be objects (not primitives).
    LIMITATIONS (unlike Map):
        - No .size
        - No iteration (no .keys, .values, .entries, .forEach, for...of)
        - No .clear
    Why? Because entries can disappear anytime via Garbage Collector, listing them is unreliable.
*/

const wm = new WeakMap();

let user = { id: 1 };
wm.set(user, "secret data 1");
wm.set(user, "secret data 2"); // Updated the existing key-value paid

console.log(wm.get(user));
console.log(wm.has(user));

user = null; // unlike Map the obj reference is null means the key-value pair is gone.

// WeakSet - Set with weak references

/**
    Values MUST be objects (not primitives).
    LIMITATIONS (unlike Set):
        - No .size
        - No iteration (no .keys, .values, .entries, .forEach, for...of)
        - No .clear
    Why? Because entries can disappear anytime via Garbage Collector, listing them is unreliable.
 */

const ws = new WeakSet();

let obj1 = { id: 1 };
let obj2 = { id: 1 }; // WeakSet (and Set) compare by reference, not content.

ws.add(obj1);
ws.add(obj2);
// ws.add("primitive"); -> stores only objects

console.log(ws.has(obj1));

obj1 = null; // unlike Set the obj reference is null means the key-value pair is gone.

console.log(ws.has(obj1))
