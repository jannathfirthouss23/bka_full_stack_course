/** NODE.JS THREADS

 WORKER THREADS
 - Communicates only via postMessage / onmessage

 CHILD PROCESS & CLUSTER
 - Child Process - spawn a separate OS process (heavier, isolated)
 - Cluster - fork multiple Node processes sharing a server port (used to scale HTTP servers across CPU cores)
 */

const { Worker } = require("worker_threads");

const nodeWorker = new Worker("./26_node_worker.js", { workerData: 1_000_000_000 });

nodeWorker.on("message", (result) => {
    console.log("Result:", result);
});
