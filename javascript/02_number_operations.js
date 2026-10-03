// ARITHMETIC OPERATORS

console.log(10 + 3);
console.log(10 - 3);
console.log(10 * 3);
console.log(10 / 3);
console.log(10 % 3);
console.log(10 ** 3);

// INCREMENT / DECREMENT

let x = 5;
x++; // post-increment
++x; // pre-increment
x--; // post-decrement
--x; // pre-decrement
console.log(x);

// ASSIGNMENT SHORTCUTS

let n = 10;
n += 5;
n -= 2;
n *= 2;
n /= 2;
n %= 5;
console.log(n);

// COMPARISON OPERATORS (returns boolean)

console.log(5 == "5"); // true (loose equality, converts type)
console.log(5 === "5"); // false (strict equality, no conversion)
console.log(5 != "5"); // false
console.log(5 !== "5"); // true
console.log(5 > 3);
console.log(5 < 3);
console.log(5 >= 5);
console.log(5 <= 4);

// LOGICAL OPERATORS (AND, OR, NOT)

console.log(true && true);
console.log(true && false);
console.log(true || false);
console.log(false || false);
console.log(!true);
console.log(!false);

// Short-circuit examples
console.log(0 || "default"); // "default" (0 is falsy, returns "default")
console.log("hi" && "bye"); // "bye" (both truthy, returns last)
console.log(null ?? "fallback"); // "fallback" (only for null/undefined)

// NUMBER METHODS

const num = 3.14159;
console.log(num.toFixed(2));
console.log(num.toString());
console.log(Number.isInteger(5));
console.log(Number.isInteger(5.5));
console.log(Number.isNaN(NaN));
console.log(Number.MAX_SAFE_INTEGER); // 9007199254740991
console.log(Number.MIN_SAFE_INTEGER); // -9007199254740991

// MATH OBJECT

console.log(Math.PI);
console.log(Math.E);

console.log(Math.round(4.6));
console.log(Math.round(4.4));
console.log(Math.floor(4.9));
console.log(Math.ceil(4.1));
console.log(Math.trunc(4.9));

console.log(Math.abs(-7));
console.log(Math.pow(2, 8));
console.log(Math.sqrt(81));
console.log(Math.cbrt(27));

console.log(Math.max(1, 5, 3, 8, 2));
console.log(Math.min(1, 5, 3, 8, 2));

console.log(Math.random()); // random number between 0 and 1

// BITWISE OPERATORS

// 5 in binary  = 0101
// 3 in binary  = 0011

console.log(5 & 3); // 1 = AND (0101 & 0011 = 0001)
console.log(5 | 3); // 7 = OR  (0101 | 0011 = 0111)
console.log(5 ^ 3); // 6 = XOR (0101 ^ 0011 = 0110)
console.log(~5); // -6 = NOT (flips all bits, becomes -(n+1))

console.log(5 << 1); // 10 = left shift (multiply by 2)
console.log(5 << 2); // 20 = left shift by 2 (multiply by 4)
console.log(20 >> 1); // 10 = right shift (divide by 2)
console.log(-20 >>> 1); // unsigned right shift

// Common bitwise trick: check if number is even or odd
console.log(10 & 1); // 0 = even
console.log(7 & 1); // 1 = odd