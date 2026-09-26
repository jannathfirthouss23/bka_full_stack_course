# A Thread runs code concurrently with other threads in the same program.

# BASIC THREAD

import threading
import time

def worker(name):
    print(f"{name} starting")
    time.sleep(0.5)
    print(f"{name} done")

t = threading.Thread(target=worker, args=("Thread-1",))
t.start()
t.join()                        # wait for it to finish

# MULTIPLE THREADS

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# LOCK (fixes race condition)
# A race condition is a bug where the result depends on which thread happens to run first

""" THREAD LOCK MECHANISM

Thread 1:   [hold lock]...release
Thread 2:   waiting.......[hold lock]...release
Thread 3:   waiting.....................[hold lock]...release
Thread 4:   waiting...................................[hold lock]...release

"""

counter = 0 # shared variable
lock = threading.Lock() # shared lock

def safe_increment():
    global counter
    with lock:
        for _ in range(100_000):
            counter += 1
        # temp = counter
        # time.sleep(0)
        # counter = temp + 1

threads = [threading.Thread(target=safe_increment) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join() # The main thread pauses here until all 4 threads have finished their work.

print(f"with lock:    {counter}")

# DAEMON vs NON-DAEMON THREAD

## DAEMON THREAD

def slow_work():
    time.sleep(2)
    print("thread done")

t = threading.Thread(target=slow_work)
t.start()
print("main done")
"""
# script reaches end here...
# Python sees thread still alive, waits silently
# thread finishes, prints "thread done"
# THEN the process exits
"""

## NON-DAEMON THREAD

t = threading.Thread(target=slow_work, daemon=True)
t.start()
print("main done")
"""
# main exits → daemon thread killed → "thread done" NEVER prints
"""
