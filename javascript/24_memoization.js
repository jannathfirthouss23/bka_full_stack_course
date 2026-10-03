// PROBLEM

function square(n) {
    console.log("Computing...");
    for (let i = 0; i < 1e7; i++) {}
    return n * n;
}

console.log(square(5)); // Computing... 25 (freshly calculated)
console.log(square(5)); // Computing... 25
console.log(square(5)); // Computing... 25

// MEMOIZED VERSION - cache the result

function memoize(fn) {
    const cache = new Map();

    return function (...args) {
        const key = JSON.stringify(args);

        if (cache.has(key)) {
            console.log("From cache");
            return cache.get(key);
        }

        const result = fn(...args);
        cache.set(key, result);
        return result;
    };
}

const fastSquare = memoize(square);

console.log(fastSquare(5)); // Computing... 25 (freshly calculated + cached)
console.log(fastSquare(5)); // Returns from cache... 25
console.log(fastSquare(7)); // Computing... 49 (freshly calculated + cached)
console.log(fastSquare(7)); // Returns from cache... 49
console.log(fastSquare(5)); // Returns from cache... 25