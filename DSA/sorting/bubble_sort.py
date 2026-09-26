arr = [64, 34, 25, 12, 22, 11, 90]

# NAIVE = O(n^2)

def bubble_sort_naive(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1): # 7 - 0 - 1
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

# print(bubble_sort_naive(arr))
