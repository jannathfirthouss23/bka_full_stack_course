# Given an array of size n, find the element that appears more than n/2 times.
import math

arr = [2, 2, 1, 1, 1, 2, 2]

# NAIVE = O(n^2)

def majority_element(nums):
    n = len(nums)
    for i in range(n):
        # count = sum(1 for x in nums if x == nums[i])
        count = 0
        for j in nums:
            x = nums[i]
            if j == x:
                count += 1
        if count > math.floor(n/2):
            return nums[i]
    return -1

print(majority_element(arr))