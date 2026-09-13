a, b = 17, 5

print(a + b, a - b, a * b)
print(a / b, a // b, a % b, a ** b)

print(a == b, a != b, a > b, a < b, a >= b, a <= b)

x, y = True, False
print(x and y)
print(x or y)
print(not x)

n = 10  # 10
n += 5  # n = n + 5
n -= 3  # 12
n *= 2  # 24
n //= 4 # 6
print(n)

print(int("42"), float("3.14"), str(100))
print(int(3.9), float(7))

print(abs(-9), round(3.789, 2), pow(2, 10))
print(min(4, 2, 7), max(4, 2, 7), sum([1, 2, 3, 4]))
print(divmod(17, 5))

print(a & b)    # 1
print(a | b)    # 21
print(a ^ b)    # 20
print(~a)       # -18
print(a << 2)   # 68
print(a >> 2)   # 4

x = 0.1 + 0.2
print(x)

import math
print(math.pi, math.sqrt(25), math.floor(4.7), math.ceil(4.2))

import random
print(random.randint(1, 10), random.random())

bin(42)
hex(255)
oct(8)
complex(2, 3)