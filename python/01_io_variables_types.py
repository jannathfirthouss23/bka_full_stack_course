print("Hello, World!")

name = "Alice" # string
age = 25 # integer
height = 5.6 # float
is_student = True # bool

print("Name:", name, "Age:", age, "Height:", height)

print(f"{name} is {age} years old and {height}ft tall")

print("Python", "is", "fun", sep="******")
print("loading", end="...")
print("\n\n\tdone")

print(type(name), type(age), type(height), type(is_student))

a, b, c = 1, 2, 3
print(a, b, c)

p = q = r = 100
print(p, q, r)

user = input("Enter your name: ")
print(f"Hello, {user}")

age_input = int(input("Enter your age: ")) # type casting
print(f"Next year you will be {age_input + 1}")

price = float(input("Enter price: "))
print(f"With 18% tax: {price * 1.18}")

n = None
print(n, type(n))

complex_num = 2 + 3j
byte_data = b"hello"

print(byte_data, type(byte_data))