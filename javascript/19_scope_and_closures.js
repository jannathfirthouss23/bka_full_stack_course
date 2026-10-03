/** SCOPE - where variables are accessible */

// GLOBAL SCOPE - accessible everywhere

const globalVar = "I am global";

function showGlobal() {
    console.log(globalVar);
}
showGlobal();

// FUNCTION SCOPE - variables inside a function stay inside

function myFunc() {
    const localVar = "I am local";
    console.log(localVar);
}
myFunc();
// console.log(localVar); ReferenceError - not accessible outside

// BLOCK SCOPE - let & const are limited to { } block except var

{
    let blockVar = "inside block";
    const alsoBlock = "also inside";
    var notBlock = "not block-scoped";
    console.log(blockVar);
}
// console.log(blockVar); Error - let is block-scoped
console.log(notBlock); // var leaks out of block

// LEXICAL SCOPE - inner functions can read outer variables

function outer() {
    const msg = "hello from outer";

    function inner() {
        console.log(msg); // can access outer's variable
    }
    inner();
}
outer();

/** CLOSURE - function remembers its outer scope */

function counter() {
    let count = 0; // this variable is "remembered"

    return function () {
        count++;
        return count;
    };
}

const c = counter();
console.log(c());
console.log(c());
console.log(c());

const c2 = counter();
console.log(c2());

// PRACTICAL USE - private variables

function createBank() {
    let balance = 0;

    return {
        deposit(amount) {
            balance += amount;
        },
        getBalance() {
            return balance;
        },
    };
}

const account = createBank();
account.deposit(500);
account.deposit(200);
console.log(account.getBalance());
// console.log(account.balance); undefined - balance is private (closure)
