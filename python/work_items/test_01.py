# LESSON 1

a = 10
b = False

print(f"a is {a}\nb is {b}") # f string

c = int(input("Enter you age: ")) # type casting & input

print(c, type(c)) # type function & double underscore

# LESSON 2

import math

x, y = 10, 20

print(y / x, y % x, y // x, math.floor(10.4999), math.ceil(10.433), round(10.6))

print(not x, x <= y, x and y)

y *= x # y = y * x

print(x, y)

# LESSON 3

name = "Hello world!"

print(f"String length = {len(name)}, Total indexes (from 0) = {len(name) - 1}")

print(name[6])
print(name[-2])
print(name[4:8])