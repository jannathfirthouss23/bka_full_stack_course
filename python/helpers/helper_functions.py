# RECURSION

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def countdown(n):
    if n <= 0:
        print("Go!")
        return
    print(n)
    countdown(n - 1)

def power_rec(base, exp):
    if exp == 0:
        return 1
    return base * power_rec(base, exp - 1)

if __name__ == "__main__":
    print("Helper loaded!") # This print should run only if current file is being run directly.