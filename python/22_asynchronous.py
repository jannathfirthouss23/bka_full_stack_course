"""
To run:
    1. Create venv `python3 -m venv async`
    2. Activate venv `async` using:
        * For macOS/linux           : source async/bin/activate
        * For windows (powershell)  : async\\Scripts\\Activate.ps1
        * For windows (cmd)         : async\\Scripts\\activate.bat
    3. Run `pip install requests`
    4. To create requirements.txt file:
        $ pip install -r requirements.txt
    5. To run this file, Make sure in venv (async): python3 async.py
"""

# Python does have an event loop. It just doesn't start automatically. So, we use `asyncio`.

"""
Event loop is the engine that reads the script line by line - but
when it hits an async/await, it sends that work off to the OS and moves on
to the next task instead of waiting, then comes back to it once the work is done.
"""

import asyncio
import time

# DEFINING AN ASYNC FUNCTION

async def greet(name):
    await asyncio.sleep(0.1)
    return f"hello, {name}"

print(asyncio.run(greet("Alice")))

# SEQUENTIAL vs CONCURRENT

async def fake_fetch(name, delay):
    print(f"  start {name}")
    await asyncio.sleep(delay)
    print(f"  done  {name}")
    return f"{name} data"

async def run_sequential():
    start = time.perf_counter() # measuring short durations
    r1 = await fake_fetch("A", 0.3)
    r2 = await fake_fetch("B", 0.3)
    r3 = await fake_fetch("C", 0.3)
    print(f"sequential: {time.perf_counter() - start:.2f}s")

async def run_concurrent():
    start = time.perf_counter()
    results = await asyncio.gather(
        fake_fetch("A", 0.3),
        fake_fetch("B", 0.3),
        fake_fetch("C", 0.3),
    )
    print(f"concurrent: {time.perf_counter() - start:.2f}s")
    print(results)

asyncio.run(run_sequential())
asyncio.run(run_concurrent())

# FETCHING DUMMY DATA

import requests

def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    return requests.get(url, timeout=5).json()

async def fetch_async(post_id):
    return await asyncio.to_thread(fetch_post, post_id)

async def fetch_one():
    post = await fetch_async(1)
    print(post["title"])

asyncio.run(fetch_one())

# FETCH MANY CONCURRENTLY

async def fetch_many(ids):
    start = time.perf_counter()
    posts = await asyncio.gather(*(fetch_async(i) for i in ids))
    # posts = await asyncio.gather(fetch_async(1), fetch_async(2), ...)
    print(f"fetched {len(posts)} posts in {time.perf_counter() - start:.2f}s")
    for p in posts:
        print(f"  {p['id']}: {p['title'][:40]}")

asyncio.run(fetch_many([1, 2, 3, 4, 5]))
