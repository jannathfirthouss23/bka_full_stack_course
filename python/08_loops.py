# FOR LOOP

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

sum = 0
for i in range(5):
    sum += i

print("sum", sum)

for i in range(2, 8): # 2 - 7
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

# ENUMERATE & ZIP

colors = ["red", "green", "blue"]

for i, c in enumerate(colors):
    print(i, c)

for i, c in enumerate(colors, start=1):
    print(i, c)

names = ["Alice", "Bob", "Carol"]
ages = [25, 30, 28]

for n, a in zip(names, ages):
    print(n, a)

# WHILE LOOP

pointer = 0

while pointer < len(colors):
    print(colors[pointer])
    pointer += 1

i = 1
while i <= 5:
    print(i)
    i += 1

n = 5
while n > 0:
    print(n)
    n -= 1

# WHILE TRUE (do-while alternative)

count = 0
while True:
    count += 1
    print(count)
    if count >= 3:
        break

# BREAK & CONTINUE

for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("CONTINUE")

p = 0

while p < len(colors):
    if (p == 1):
        p += 1
        continue

    print(colors[p])
    p += 1

# p = 0
# p = 1
# p = 2

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

# COMPREHENSION

nums = [1, 2, 3, 4, 5]

squares = [x * x for x in nums] # [1, 4, 9, 16, 25]
print(squares)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)

words = ["hello", "world", "python"]

upper = [w.upper() for w in words]
print(upper)

miss = [c for c in "mississippi"]
print(miss)

unique = {c for c in "mississippi"}
print("unique", unique)

square_map = {"x": x * x for x in range(1, 6)} # { x: 1, x: 4, x: 9, x: 16, x: 25 } = { x: 25 }
print(square_map)

square_map2 = {x: x * x for x in range(1, 6)} # { 1: 1, 2: 4, 3: 9, 4: 16, 5: 25 }
print(square_map2)

# NESTED LOOP

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

# FOR-ELSE

target = 7
for n in [1, 3, 5, 9]:
    if n == target:
        print("found")
        break
else:
    print("not found")