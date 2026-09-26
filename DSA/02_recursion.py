from django.db.models.fields import return_None

nums = [1,2,3,4,5]

def hi():
    bye()
    print("Hello world")

def bye():
    print("Bye world")

hi()

print("="*50)

# for num in nums:
#     print(num)

def pnum(nums, i):
    if i >= len(nums): return
    print(nums[i]) # 1
    pnum(nums, i+1)

pnum(nums, 0)

print("="*50)

def print_num(num, i):
    if i >= len(num): return
    print_num(num, i + 1)
    print(num[i])

print_num(nums, 0)

# FACTORIAL - 12345

def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print("fact", fact(0))

from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# FIBONACCI - 0,1,1,2,3,5,8

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(6))

# PALINDROME

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

s = "racecar"
print(s[1:]) # Remove first letter
print(s[:-1]) # Remove last letter

print(is_palindrome('racecar'))

# SUBSET SUM

"""
    fn(arr,3,25) = [10,20,15]
    |----------fn(arr,2,25) = [10,20]
    |                |------fn(arr,1,25) = [10], sum = 25
    |                |        |---fn(arr,0,25)  = return 0
    |                |        |---fn(arr,0,25-10) = return 0 (sum = 15)
    |                |
    |                |------fn(arr,1,25-20) = [10], sum = 5
    |                         |---fn(arr,0,5) = return 0
    |                         |---fn(arr,0,5-10) = return 0 (sum = -5)
    |
    |----------fn(arr,2,25-15) = [10,20], sum = 10
                   |------fn(arr,1,10) = [10]
                   |        |---fn(arr,0,10) = return 0
                   |        |---fn(arr,0,10-10) = return 1 (sum = 0)
                   |
                   |------fn(arr,1,10-15) = [10]
                            |---fn(arr,0,-5) = return 0
                            |---fn(arr,0,-5-10) = return 0 (sum = -15)    
"""

def count_subsets(arr, n, sum):
    if n == 0:
        return 1 if sum == 0 else 0
    return count_subsets(arr, n - 1, sum) + count_subsets(arr, n - 1, sum - arr[n - 1])

print(count_subsets([10, 20, 15], 3, 25))