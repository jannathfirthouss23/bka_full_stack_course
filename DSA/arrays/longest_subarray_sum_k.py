# Given an array of integers and a target sum K, find the length of the longest subarray whose elements add up to exactly K.

arr = [1, -1, 5, -2, 3]

# [5, -2] = 2
# [3] = 1
# [1, -1, 5, -2] = 4

# NAIVE = O(n^2)

def longest_subarray_sum_k(nums, k):
    n = len(nums)
    longest = 0
    for i in range(n):
        running = 0
        for j in range(i, n):
            running += nums[j]
            if running == k: # j =3 & i =0
                longest = max(longest, j - i + 1) # max(0, 3 - 0 + 1) = 4
    return longest

print(longest_subarray_sum_k(arr, 3))