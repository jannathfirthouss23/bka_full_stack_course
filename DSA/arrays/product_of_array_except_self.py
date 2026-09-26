# Given an array, return a new array where each element at index i is the product of all elements except the one at i.

arr = [1, 2, 3, 4]

# NAIVE = O(n^2)

def product_except_self(nums):
    n = len(nums)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    return result

print(product_except_self(arr))