# Given an array, find all unique triplets that add up to 0.

arr = [-1, 0, 1, 2, -1, -4]

# NAIVE = O(n^3)

def three_sum(nums):
    n = len(nums)
    found = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    found.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(t) for t in found]

print(three_sum(arr))