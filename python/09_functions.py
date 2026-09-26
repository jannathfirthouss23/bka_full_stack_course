# BASIC FUNCTION

def greet():
    print("Hello!")

greet()
greet()

def greet_name(name): # name is called parameter
    print(f"Hello, {name}!")

greet_name("Alice") # "Alice" is called argument
greet_name("Bob")

# RETURN VALUES

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([4, 7, 1, 9, 3])
print(lo, hi)

# DEFAULT ARGUMENTS

def power(base, exp=2):
    return base ** exp

print(power(5))         # 25
print(power(5, 3))      # 125

# KEYWORD ARGUMENTS

def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe("Alice", 25, "Boston")
describe(age=25, city="Boston", name="Alice")
describe("Alice", city="Boston", age=25)

# *ARGS (variable positional)

def total(*nums):
    print(nums)             # tuple
    return sum(nums)

print(total(1, 2, 3))
print(total(1, 2, 3, 4, 5))
print(total(*[10, 20, 30]))

# **KWARGS (variable keyword)

def build_profile(**info):
    print(info)             # dict
    for k, v in info.items():
        print(k, "->", v)

build_profile(name="Alice", age=25, city="Boston")

# MIXED

def mixed(a, b, *args, key="default", **kwargs):
    print(a, b)
    print(args)
    print(key)
    print(kwargs)

mixed(1, 2, 3, 4, 5, key="custom", extra1="x", extra2="y")

# POSITIONAL-ONLY & KEYWORD-ONLY

def strict(a, b, /, c, *, d):
    return a + b + c + d

print(strict(1, 2, 3, d=4))

from helpers.helper_functions import factorial, fib, countdown, power_rec

print(factorial(5))                    # 120
print(factorial(7))                    # 5040
print(fib(10))                         # 55
countdown(3)
print(power_rec(2, 10))     # 1024
