# Given an array of integers and a target K, find the total number of subarrays whose sum equals K.

arr = [1, 2, 3]

# NAIVE = O(n^2)

def subarray_sum(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        running = 0
        for j in range(i, n):
            running += nums[j]
            if running == k:
                count += 1
    return count

print(subarray_sum(arr, 3))