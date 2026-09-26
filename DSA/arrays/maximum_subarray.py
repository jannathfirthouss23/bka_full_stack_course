# Given an array of integers, find the subarray with the largest sum.

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# NAIVE = O(n^2)

def max_subarray(nums):
    best = float("-inf")
    n = len(nums)
    for i in range(n):
        running = 0
        for j in range(i, n):
            running += nums[j]
            best = max(best, running)
    return best

print(max_subarray(arr))