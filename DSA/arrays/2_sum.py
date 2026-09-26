# Given an array and a target, find two numbers that add up to the target. Return their indices.

nums = [2, 11, 7, 7, 4, 15]
target = 9

# NAIVE = O(n^2)

def two_sum_naive(nums, target):
    n = len(nums)

    for i in range(n):
        # start of i....
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
        # end of i....
    return []

two_sum_naive(nums, target)

# EFFICIENT = O(n)

"""
{}

need = 9 - 2 = 7
{2: 0}

need = 9 - 7 = 2
{7: 1}

return [0, 1]
"""
nums = [2, 11, 7, 7, 4, 15]
target = 9
def two_sum_efficient(nums, target):
    store = {}
    for i, num in enumerate(nums):
        remaining = target - num
        if remaining in store:
            return [store[remaining], i]
        store[num] = i
    return []

two_sum_efficient(nums, target)