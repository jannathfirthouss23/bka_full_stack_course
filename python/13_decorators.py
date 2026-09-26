# BASIC DECORATOR

def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")

    return wrapper

def greet():
    print("Hello!")

greet = my_decorator(greet)
greet()

# WITH @ SYNTAX

@my_decorator
def say_hi():
    print("Hi!")

say_hi()

# DECORATOR WITH ARGUMENTS

def log(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"got {result}")
        return result

    return wrapper

@log
def add(a, b):
    return a + b

add(3, 4)

# DECORATOR WITH PARAMETERS

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator

@repeat(3)
def hello(name):
    print(f"Hello, {name}")

hello("Alice")