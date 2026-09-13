# Lesson 1: Variables and Data Types
"Hello, World!"
print("Hello, World!") # output

print(1 + 1) 
print(2+2)
print(1+1, 2+2)

name = "Alice" #variable = Values
age = 24
height = 5.5
is_major = True
has_cancer = None

print(name, age, height, is_major, has_cancer) # output
print(name + ",", age)
print(name + " in Wonderland")

print(name, ":", age, ":", height, ":", is_major, ":", has_cancer)

print("name :", name) 
print("age :", age)
print("height :", height)

print("name :", name, "age :", age, "height :", height, "is_major :", is_major, "has_cancer :", has_cancer)

print("name :", name, "\nage :", age, "\nheight :", height, "\nis_major :", is_major, "\nhas_cancer :", has_cancer)

print("name :", name, "\t\tage :", age)

print(f"Name: {name}, Age: {age}, Height: {height}, Is Major: {is_major}, Has Cancer: {has_cancer}") # f string

# print(), # Function 1
# type(), # Function 2

x = type(name)
print(x)

y = type(age)
print(y)

z = type(height)
print(z)

u = type(is_major)
print(u)

v = type(has_cancer)
print(v)



# print(), # Function 1
# type(), # Function 2
# input(), # Function 3
# int(), # Function 4
# float(), # Function 5


namex = input("Enter your name: ") # input function 
print(namex)

namex = input("Enter your name: ") # input function
print(f"so. your name is {namex}")

agex = int(input("Enter your age: ")) # type casting & input function
print(f"so. your age is {agex}")

print(type(agex)) # type function & double underscore

heightx = float(input("Enter your height: ")) # type casting & input function
print(f"so. your height is {heightx}")

print(type(heightx)) # type function & double underscore

# Data Types in Python

# String = "Hello, World!"
# Integer = 24
# Float = 5.5 Decimal value (.00)
# Boolean = True or False
# None = None

# this all variables are called as data types in python.