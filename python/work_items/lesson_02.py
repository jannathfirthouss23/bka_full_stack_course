# Lesson 2: Number Operations
a, b = 17,5
print(a + b, a - b, a * b, a / b, a**b, a % b)

# print(a + b)   # 22
# print(a - b)   # 12
# print(a * b)   # 85
# print(a / b)   # 3.4
# print(a // b)  # 3
# print(a % b)   # 2
# print(a ** b)  # 1419857

a, b = 17, 5
print(a == b, a != b, a > b, a < b, a >= b, a <= b)
# print(a == b)   # False
# print(a != b)   # True
# print(a > b)    # True
# print(a < b)    # False
# print(a >= b)   # True
# print(a <= b)   # False

# and, or, not. 

# and
# x = True, + # 1
# y = False  = # 

x, y = True, False
# True  and True   → True
# True  and False  → False
# False and True   → False
# False and False  → False

print(x and y)  # False @ 1 and 0
print(x and x)  # True  @ 1 and 1
print(y and x) # False @ 0 and 1
print(y and y)  # False @ 0 and 0

# or
# x or y  →  True or False  →  True
# True  or True   → True
# True  or False  → True
# False or True   → True
# False or False  → False

print(x or y)   # True  @ 1 or 0
print(x or x)   # True  @ 1 or 1
print(y or x)   # True @ 0 or 1
print(y or y)   # False @ 0 or 0 

# not
# not x  →  not True  →  False
print(not x)    # False @ not 1
print(not y)    # True @ not 0


# compound assignment operators — n
# n = 10
# n = 10 + 5  →  n = 15
# n = 15 - 3  →  n = 12  @ 10+5-3 = 12
# n = 12 * 2  →  n = 24  @ 12 * 2 % 4 = 6
# n = 24 // 4 →  n = 6 

n = 10       # n = 10
n += 5       # n = 15
n -= 3       # n = 12
n *= 2       # n = 24
n //= 4      # n = 6
# print(n)     # 6

# n = 0 
# k = 10 (n + 10) + (n -10)  # k = 10
# n = 0 
# k = n + 10

# print(n) # 0
# print(k) # 10

n = 0
n = n + 5 
k = n / 5  # 5 % 5 = 1.0
n = a      # a = 17
n *= 100   # n = n * 100 
print (n, k)  # 100.0 10