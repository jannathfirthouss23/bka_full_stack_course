# LOOPS

fruits = ["apple", "banana", "cherry"]
colors = ["red", "green", "blue"]

for x in fruits:
    print(x)

for x in range(1,6,2):
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


# For Ashif


pointer = 0
while pointer < len(fruits):
    if pointer == 2:
        pointer = pointer + 1
        continue
    print(fruits[pointer])
    pointer = pointer + 1
    # EOF

print("="*50)

for i in range(1, 4):
    print("Started J loop for i =", i)
    for j in range(5, 8):
        print(f"{i} * {j} =", i * j)
    print("Finished J loop")