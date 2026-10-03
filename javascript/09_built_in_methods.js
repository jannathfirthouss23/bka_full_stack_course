// JSON METHODS

const user = { name: "Alice", age: 25 };

const jsonStr = JSON.stringify(user);
console.log(jsonStr);

const userObj = JSON.parse(jsonStr);
console.log(userObj);
console.log(userObj.name);

console.log(JSON.stringify(user, null, 2));

// DATE METHODS

const now = new Date();
console.log(now);

console.log(now.getFullYear());
console.log(now.getMonth());
console.log(now.getDate());
console.log(now.getDay());
console.log(now.getHours());
console.log(now.getMinutes());
console.log(now.getSeconds());

console.log(now.toISOString());
console.log(now.toDateString());
console.log(now.toLocaleDateString());

console.log(Date.now());

const birthday = new Date("2000-01-15");
console.log(birthday.getFullYear());

const timeoutId = setTimeout(() => {
    console.log("Runs after 2 seconds");
}, 2000);

clearTimeout(timeoutId);

// setInterval - run code repeatedly at intervals
const intervalId = setInterval(() => {
    console.log("Runs every 1 second");
}, 1000);

setTimeout(() => {
    clearInterval(intervalId);
    console.log("Interval stopped");
}, 5000);
