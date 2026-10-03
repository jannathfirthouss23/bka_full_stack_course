// Listen for messages from the main thread
self.onmessage = (e) => {
    const n = e.data;

    // Heavy computation that would freeze the UI if done on main thread
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum += i;
    }

    // Send result back to main thread
    self.postMessage(sum);
};