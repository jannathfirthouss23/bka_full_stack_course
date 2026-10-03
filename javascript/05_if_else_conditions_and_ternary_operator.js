const age = 18;

if (age >= 18) {
    console.log("You are an adult");
}

const isRaining = true;

if (isRaining) {
    console.log("Take an umbrella");
} else {
    console.log("Enjoy the sun");
}

const score = 75;

if (score >= 90) {
    console.log("Grade: A");
} else if (score >= 75) {
    console.log("Grade: B");
} else if (score >= 60) {
    console.log("Grade: C");
} else {
    console.log("Grade: F");
}

const userAge = 20;
const hasLicense = true;

if (userAge >= 18) {
    if (hasLicense) {
        console.log("You can drive");
    } else {
        console.log("Get a license first");
    }
} else {
    console.log("Too young to drive");
}

const temperature = 25;
const isSunny = true;

if (temperature > 20 && isSunny) {
    console.log("Perfect weather!");
}

if (temperature > 30 || temperature < 10) {
    console.log("Extreme weather");
}

if (!isRaining) {
    console.log("No rain today");
}

if ("hello") console.log("non-empty string is truthy");
if (1) console.log("non-zero number is truthy");
if ([]) console.log("empty array is truthy");
if ({}) console.log("empty object is truthy");

// if (0)    = won't run
// if ("")   = won't run
// if (null) = won't run

const userType = age >= 18 ? "Adult" : "Minor";
console.log(userType);

const message = isRaining ? "Stay home" : "Go out";
console.log(message);

const grade = score >= 90 ? "A" : score >= 75 ? "B" : score >= 60 ? "C" : "F";
console.log(grade);

// NULLISH COALESCING (??) - fallback for null or undefined

const username = null;
console.log(username ?? "Guest");

const count = 0;
console.log(count ?? 10);
console.log(count || 10);

// SHORT-CIRCUIT EVALUATION (shortcut for if)

const isLoggedIn = true;
isLoggedIn && console.log("Welcome back!");

const name = "" || "Anonymous";
console.log(name);