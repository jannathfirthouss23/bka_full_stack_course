# apply() is HOF because it receives a function as a parameter & may or maynot return that function.
# square() is callback because it is passed into another function.

def apply(func, value):
    return func(value)

def square(x):
    return x * x

def cube(x):
    return x ** 3

print(apply(square, 5))         # 25
print(apply(cube, 3))           # 27

# FUNCTION RETURNING A FUNCTION

def multiplier(n):
    def inner(x):
        return x * n
    return inner

double = multiplier(2)
triple = multiplier(3)

print(double(7))                # 14
print(triple(7))                # 21

# BUILT-IN HOFs: MAP, FILTER, SORTED

nums = [1, 2, 3, 4, 5]

def is_even(n):
    return n % 2 == 0

def to_square(n):
    return n * n

print(list(map(to_square, nums)))       # [1, 4, 9, 16, 25]
print(list(filter(is_even, nums)))      # [2, 4]

# SORT WITH KEY FUNCTION

people = [("Alice", 30), ("Bob", 25), ("Carol", 35)]

def by_age(p):
    return p[1]

def by_name(p):
    return p[0]

print(sorted(people, key=by_age))
print(sorted(people, key=by_name))

# FUNCTIONS IN A LIST

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

operations = [add, sub, mul]

for op in operations:
    print(op(10, 3))

# FUNCTIONS IN A DICT (dispatch table)

calc = {
    "add": add,
    "sub": sub,
    "mul": mul,
}

print(calc["add"](10, 5))
print(calc["mul"](4, 3))

# CALLBACK IN ACTION (event-style)

def on_success(data):
    print(f"success: {data}")

def on_failure(error):
    print(f"failure: {error}")

def fetch(value, success_cb, failure_cb):
    if value > 0:
        success_cb(value)
    else:
        failure_cb("invalid value")

fetch(100, on_success, on_failure)
fetch(-1, on_success, on_failure)