/** ITERATORS
        - How for...of works behind the scenes (calls .next() until done: true)
        - Strings, arrays, maps, sets are all built-in iterables
        - The iterator protocol - next() returning {value, done} & [Symbol.iterator]() method
*/

const arr = [10, 20, 30];

// for...of uses iterators
for (const num of arr) {
    console.log(num); // 10, 20, 30
}

// spread uses iterators
console.log([...arr])

// iterators
const iterator = arr[Symbol.iterator]();

console.log(iterator.next()); // { value: 10, done: false }
console.log(iterator.next()); // { value: 20, done: false }
console.log(iterator.next().value); // { value: 30, done: false }
console.log(iterator.next()); // { value: undefined, done: true }

const it = "abc"[Symbol.iterator]();
console.log(it.next()); // { value: "a", done: false }
console.log(it.next()); // { value: "b", done: false }

// CUSTOM ITERATOR

const range = {
    start: 1,
    end: 5,
    [Symbol.iterator]() {
        let current = this.start;
        const end = this.end;

        return {
            next() {
                if (current <= end) {
                    return { value: current++, done: false };
                }
                return { value: undefined, done: true };
            },
        };
    },
};

for (const n of range) {
    console.log(n);
}
console.log([...range]);

/** GENERATORS
        - It is a special function that can PAUSE and RESUME
        - A cleaner way to make CUSTOM ITERATORS
        - function* syntax with yield
*/

// function*

function* simpleGen() {
    yield "a";
    yield "b";
    yield "c";
}

const gen = simpleGen();

console.log(gen.next()); // { value: "a", done: false }
console.log(gen.next()); // { value: "b", done: false }
console.log(gen.next()); // { value: "c", done: false }
console.log(gen.next()); // { value: undefined, done: true }

for (const ch of simpleGen()) {
    console.log(ch);
}
console.log("gen", [...simpleGen()])

// yield

function* range2(start, end) {
    for (let i = start; i <= end; i++) {
        yield i; // Never computes the next value until .next()
    }
}

for (const n of range2(1, 5)) { // for...of automatically calls .next()
    console.log(n);
}

console.log([...range2(10, 13)]); // spread automatically calls .next()

// yield* - unfolds another iterable, producing all its values one by one

function* letters() {
    yield "a";
    yield "b";
}

function* numbers() {
    yield 1;
    yield 2;
}

function* combined() {
    yield* letters();
    yield* numbers();
    yield "end";
}

console.log([...combined()]); // ["a", "b", 1, 2, "end"]