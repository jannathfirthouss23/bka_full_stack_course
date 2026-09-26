# Given an array, move all 0s to the end while keeping the order of non-zero elements the same.

arr = [0, 1, 0, 3, 12]

# NAIVE = O(n^2)

def move_zeroes(nums):
    n = len(nums)
    for _ in range(n):
        for j in range(n - 1):
            if nums[j] == 0 and nums[j + 1] != 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print(move_zeroes(arr))