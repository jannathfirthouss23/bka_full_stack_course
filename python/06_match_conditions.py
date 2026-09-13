code = 404

match code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown")

status = 302

match status:
    case 301 | 302 | 307:
        print("redirect")
    case 200 | 201 | 204:
        print("success")
    case _:
        print("other")

point = (0, 5)

match point:
    case (0, 0):
        print("origin")
    case (0, y):
        print(f"on Y-axis at {y}")
    case (x, 0):
        print(f"on X-axis at {x}")
    case (x, y):
        print(f"point ({x}, {y})")

args = ["git", "commit", "-m", "msg"]

match args:
    case []:
        print("no command")
    case [only]:
        print(f"single: {only}")
    case [cmd, *rest]:
        print(f"cmd={cmd}, args={rest}")

event = {"type": "click", "x": 10, "y": 20}

match event:
    case {"type": "click", "x": x, "y": y}:
        print(f"click at ({x},{y})")
    case {"type": "key", "key": k}:
        print(f"key: {k}")
    case {"type": t}:
        print(f"unknown type: {t}")
    case _:
        print("invalid")

n = -5

match n:
    case x if x < 0:
        print("negative")
    case 0:
        print("zero")
    case x if x < 10:
        print("small")
    case _:
        print("large")