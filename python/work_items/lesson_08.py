# lesson 08

# LOOPS

fruits = ["apple", "banana", "cherry", "grape"]
colors = ["red", "green", "blue", "purple"]

for x in fruits:
    print(x)

#sum
for x in range(1,6):
    print(x)

for i, x in enumerate(fruits):
    print(f"{i}: {x}")

for x, y in zip(fruits, colors):
    print(x, y)

i = 1
while i >= 1 and i <= 5:
    print(i)
    i = i + 1
    # EOF

# WHILE LOOP
pointer = 0
while pointer < len(colors):
    print(colors[pointer])
    pointer += 1

# BREAK & CONTINUE
pointer = 0
while pointer < len(fruits):
    if pointer == 2:
        continue
    print(fruits[pointer]) # outpuut apple
    pointer = pointer + 1
     # EOF

# 0 < 3: apple, 1+
# 1 < 3: banana, 1+
# 2 < 3: 