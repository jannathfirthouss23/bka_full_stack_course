# INNER FUNCTION

def outer():
    print("outer running")

    def inner():
        print("inner running")

    inner()

# inner() is not accessible outside outer()
# inner()       # NameError
outer()

# CLOSURE: INNER REMEMBERS OUTERS VARIABLES

def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"

    return greet

hi = make_greeter("Hi")
hello = make_greeter("Hello")

print(hi("Alice"))  # Hi, Alice!
print(hello("Bob"))  # Hello, Bob!

# NONLOCAL vs GLOBAL

def outer_read():
    msg = "hello"

    def inner():
        print(msg)  # works without nonlocal

    inner()

outer_read()

def outer_write():
    msg = "hello"

    def inner():
        nonlocal msg
        msg = "changed"  # needs nonlocal to reassign

    inner()
    print(msg)  # changed

outer_write()