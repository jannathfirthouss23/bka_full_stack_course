arr = [64, 25, 12, 22, 11]

# NAIVE = O(n^2)

def selection_sort_naive(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

print(selection_sort_naive(arr))
