const day = "Mon";

switch (day) {
    case "Mon":
        console.log("Monday");
        break;
    case "Tue":
        console.log("Tuesday");
        break;
    case "Wed":
        console.log("Wednesday");
        break;
    default:
        console.log("Other day");
}

// MULTIPLE CASES (fall-through on purpose)

const today = "Sat";

switch (today) {
    case "Mon":
    case "Tue":
    case "Wed":
    case "Thu":
    case "Fri":
        console.log("Weekday");
        break;
    case "Sat":
    case "Sun":
        console.log("Weekend");
        break;
    default:
        console.log("Invalid day");
}

// SWITCH WITH NUMBERS

const grade = 2;

switch (grade) {
    case 1:
        console.log("First place 🥇");
        break;
    case 2:
        console.log("Second place 🥈");
        break;
    case 3:
        console.log("Third place 🥉");
        break;
    default:
        console.log("No medal");
}

// FORGETTING BREAK (causes fall-through)

const color = "red";

switch (color) {
    case "red":
        console.log("Red"); // runs
    case "blue":
        console.log("Blue"); // also runs (no break above)
        break;
    case "green":
        console.log("Green");
        break;
}