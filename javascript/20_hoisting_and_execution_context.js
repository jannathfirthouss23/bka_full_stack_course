/**
 * GLOBAL EXECUTION CONTEXT (GEC) - An empty object globally that stores everything needs to run code.
 * GEC = {
 *   variableEnvironment: {
 *     x: 10,
 *     y: 10,
 *     z: 10,
 *     sayHi: <function>,
 *   },
 *   this: window,
 *   outer: null,
 * }
 *
 * GEC has Two phases:
 *      Memory / Creation phase: variables & functions get registered (hoisted) in RAM
 *      Execution phase: code runs line by line
 *
 * In memory phase:
 * x      -> undefined         (var is hoisted with undefined)
 * y      -> empty
 * z      -> empty
 * sayHi  -> full function code stored
 *
 * In execution phase:
 * x       -> 10
 * y       -> 10
 * z       -> 10
 * sayHi() -> runs when called
 * */

console.log(this); // window
var x = 10;
let y = 10;
const z = 10;
function sayHi() {
    console.log("Hi");
}
// Once a function is stored in a variable or used arrow function then it is not hoisted
// var sayVarHi = () => {
//     console.log("Hi");
// }

/**
 * FUNCTION EXECUTION CONTEXT (FEC) - Created EVERY TIME a function is called &
 * has its own memory for parameters and local variables
 * */

function multiply(a, b) { // no FEC created here
    let result = a * b;
    return result;
}

multiply(2, 5); // FEC for multiply(2,5) created here, pushed to stack, popped when done
multiply(3, 4); // FEC for multiply(3,4) created here, pushed to stack, popped when done

// FEC has no variable called "qwerty", so it looks into GEC

let qwerty = 10;

function test() {
    // no `qwerty` declared here
    console.log(qwerty);
}
test();

/**
 * CALL STACK - LIFO stack of execution contexts
 * */

function one() {
    console.log("one start");
    two();
    console.log("one end");
}

function two() {
    console.log("two start");
    three();
    console.log("two end");
}

function three() {
    console.log("three start");
    console.log("three end");
}

one();

// Output order:
//      - one start
//      - two start
//      - three start
//      - three end
//      - two end
//      - one end

// Call Stack:
//   [GEC]                    <- script starts, then pushes
//   [GEC, one]               <- logs "one start" & pushes two()
//   [GEC, one, two]          <- logs "two start" & pushed three()
//   [GEC, one, two, three]   <- logs "three start" & "three end", then pops
//   [GEC, one, two]          <- logs "two end", then pops
//   [GEC, one]               <- logs "one end", then pops
//   [GEC]                    <- script finishes, then pops
//   []

/**
 * Stack Overflow - When the call stack grows too deep (e.g., infinite recursion)
 * */

function blowUp() {
    blowUp();
}
// blowUp(); // RangeError: Maximum call stack size exceeded

/**
 * Heap - Bigger or un-predictable in size (objects, arrays, functions) then JS uses the heap
 * apart from CALL STACK it is small, fixed-size memory area.
 *
 *           CALL STACK                                HEAP
 *             [GEC]
 *            x = 10
 *         arr: -> 0x9001            |            0x9001: [1, 2, 3]
 *         user: -> 0x9002           |         0x9002: { name: "Alice" }
 * */

// PRIMITIVES copy the value

let a = 5;
let b = a;
b = 99;
console.log(a);

// OBJECTS copy the address (reference)

let obj1 = { name: "Alice" };
let obj2 = obj1;
obj2.name = "Bob";
console.log(obj1.name);

// INSTANCE vs REFERENCE

/**
 * Instance - The actual value created in memory (lives in heap)
 * Reference - The address that points to that object (held by a variable)
 *
 *    STACK (reference)             HEAP (instance)
 *      n -> 0x9001       |     0x9001: { value: "Rex" }
 *      n = 0
 *
 * Real-life analogy: Imagine address is "123 Main St".
 *
 * Instance = actual house
 * Reference = the address ("123 Main St")
 * */
