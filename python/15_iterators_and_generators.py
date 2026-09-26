# ITER & NEXT

nums = [10, 20, 30]

it = iter(nums)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# next(it)                      # StopIteration

# GENERATOR FUNCTION (yield instead of return)
# Each yield pauses the function and hands a value to the caller & then call resumes right after the yield.

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)

# GENERATOR EXPRESSION
# Same as list comprehension but with () instead of []

squares = (x * x for x in range(5))
print(squares)  # <generator object>
print(list(squares))  # [0, 1, 4, 9, 16]


# READING A FILE LAZILY USING GENERATOR

# def read_lines(path):
#     with open(path) as f:
#         for line in f:
#             yield line.rstrip()
