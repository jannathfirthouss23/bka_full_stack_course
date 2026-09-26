# LAMBDA (anonymous function)

square = lambda x: x * x
print(square(5))

add = lambda a, b: a + b
print(add(3, 4))

print(sorted([("Alice", 30), ("Bob", 25)], key=lambda p: p[1]))

# REDUCE (Map/Accumulator)

from functools import reduce

nums = [1, 2, 3, 4, 5]

print(reduce(lambda a, b: a + b, nums))             # 15
print(reduce(lambda a, b: a * b, nums))             # 120
print(reduce(lambda a, b: a if a > b else b, nums)) # 5
print(reduce(lambda acc, x: acc + x, nums, 100))    # 115 (with initial value = 100)

# PARTIAL (pre-fills some of its arguments)

from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2) # Pre-fills exp=2
cube = partial(power, exp=3) # Pre-fills exp=3

print(square(5))                            # 25
print(cube(4))                              # 64

# ITERTOOLS

from itertools import count, cycle, chain, islice, takewhile, groupby

# islice - Slice operator
# count - infinite counter
print(list(islice(count(10, 2), 5)))        # [10, 12, 14, 16, 18]

# cycle - repeats forever
print(list(islice(cycle("AB"), 6)))         # ['A', 'B', 'A', 'B', 'A', 'B']

# chain - flatten multiple iterables
print(list(chain([1, 2], [3, 4], [5])))     # [1, 2, 3, 4, 5]

# takewhile - take while condition
print(list(takewhile(lambda x: x < 5, [1, 3, 5, 2])))   # [1, 3]

# groupby - group consecutive equal elements
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("c", 5)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))

# OPERATOR

import operator

print(operator.add(10, 5))                  # 15
print(operator.mul(4, 3))                   # 12
print(operator.lt(3, 5))                    # True

# operator with reduce (cleaner than lambdas)
print(reduce(operator.add, nums))           # 15
print(reduce(operator.mul, nums))           # 120
