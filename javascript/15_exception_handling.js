// try / catch with throw

try {
    throw new Error("Something went wrong");
} catch (err) {
    console.log("Caught:", err.message);
}

// try / catch / finally

try {
    throw new Error("Oops");
} catch (err) {
    console.log("Caught:", err.message);
} finally {
    console.log("Finally runs always");
}