// JS is SINGLE-THREADED - only one piece of code runs at a time on the main thread.
// But NODE.js & Browser runtimes provide ways to do work in parallel on REAL OS threads.

/** BROWSER THREADS

    WEB WORKER
        - Doesn't touch the DOM
        - Communicates only via postMessage / onmessage
        - Each worker has its own memory (no shared variables)

    OTHER BROWSER WORKER TYPES:
        - Service Worker - runs in background, intercepts network requests (used for PWAs, offline caching, push notifications)
        - Shared Worker  - shared by multiple tabs/iframes of the same origin
*/

const browserWorker = new Worker("25_web_worker.js");

// Listen for messages FROM the worker
browserWorker.onmessage = (e) => {
    console.log("Result from worker:", e.data);
};

// Send a message TO the worker
document.getElementById("startBtn").addEventListener("click", () => {
    console.log("Sending heavy task to worker...");
    browserWorker.postMessage(1_000_000_000); // huge number - would freeze main thread
});

// While the worker is computing, the UI stays responsive
document.getElementById("uiBtn").addEventListener("click", () => {
    console.log("UI button still works while worker runs!");
});

// worker.terminate();
