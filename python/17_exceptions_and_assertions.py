# BASIC TRY/EXCEPT

try:
    x = 1 / 0
except Exception as e:
    print("Error: ", e)

try:
    x = int("abc")
except ValueError as e:
    print("caught:", e)

# MULTIPLE EXCEPTIONS

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "cannot divide by zero"
    except TypeError:
        return "wrong types"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "a"))

# TRY / EXCEPT / ELSE / FINALLY
"""
# try    - code that might fail
# except - runs if an error happens
# else   - runs if NO error happened
# finally- always runs (cleanup)
"""

try:
    result = 10 / 2
except ZeroDivisionError:
    print("error")
else:
    print("no error, result =", result)
finally:
    print("always runs")

# RAISING EXCEPTIONS

def set_age(age):
    if age < 0:
        raise ValueError(f"age cannot be negative, got {age}")
    return age

try:
    set_age(-5)
except ValueError as e:
    print("caught:", e)

# CUSTOM EXCEPTIONS

class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"balance {balance} cannot cover {amount}")
    return balance - amount

try:
    withdraw(100, 500)
except InsufficientFundsError as e:
    print("caught:", e)

# ASSERTIONS

def average(numbers):
    assert len(numbers) > 0, "list cannot be empty"
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4]))

try:
    average([])
except AssertionError as e:
    print("caught:", e)