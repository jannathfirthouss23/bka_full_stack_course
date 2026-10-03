// FOR LOOP

for (let i = 0; i < 5; i++) {
    console.log(i);
}

// WHILE LOOP

let n = 0;
while (n < 3) {
    console.log("while:", n);
    n++;
}

// DO...WHILE LOOP

let k = 5;
do {
    console.log("do-while:", k);
    k++;
} while (k < 3);

// FOR...OF LOOP - iterates over (arrays, strings)

const fruits = ["apple", "banana", "cherry"];
for (const fruit of fruits) {
    console.log(fruit);
}

for (const char of "abc") {
    console.log(char); // a, b, c
}

// FOR...IN LOOP - iterates over keys (objects)

const user = { name: "Alice", age: 25, city: "Paris" };
for (const key in user) {
    console.log(key, "=", user[key]);
}

// BREAK - exits the loop immediately

for (let i = 0; i < 10; i++) {
    if (i === 3) break;
    console.log("break:", i);
}

// CONTINUE - skips current iteration, moves to next

for (let i = 0; i < 5; i++) {
    if (i === 2) continue;
    console.log("continue:", i);
}

// NESTED LOOPS

for (let i = 1; i <= 3; i++) {
    for (let j = 1; j <= 3; j++) {
        console.log(`i=${i}, j=${j}`);
    }
}
