const { parentPort, workerData } = require("worker_threads");

let sum = 0;
for (let i = 0; i < workerData; i++) sum += i;

parentPort.postMessage(sum);