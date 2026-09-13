# For Ashif

# FUNCTIONS

def printing(name):
    print(f"Hello {name}")

def addition(a, b = 1):
    return a + b

printing("Alice")
printing("Bob")

x = addition(1)
y = addition(2, 2)
z = addition(3, 3)

print(x, y, z)

# EXCEPTIONS

try:
    print(10/0)
    # print(10/1)
except Exception as error:
    print(error)

print("Hello world")

# CLASS - OOPS

class Math:
    PI = 3.1415926 # Instance

    def __init__(self, a, b): # Constructor (optional)
        self.a = a
        self.b = b

    def addition(self): # Method
        return self.a + self.b

    def subtraction(self): # Method
        return self.a - self.b

    def multiplication(self): # Method
        return self.a * self.b

    def division(self, b): # Method
        return self.a / b

    def pi(self): # Method
        return Math.PI

math_1 = Math(1, 2)
a = math_1.addition()
b = math_1.subtraction()
c = math_1.multiplication()
d = math_1.division(10)
e = math_1.pi()

print(a, b, c, d, e, Math.PI)