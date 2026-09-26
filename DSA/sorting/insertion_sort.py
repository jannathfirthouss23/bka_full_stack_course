arr = [12, 11, 13, 5, 6]

# NAIVE = O(n^2)

def insertion_sort_naive(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

print(insertion_sort_naive(arr))
