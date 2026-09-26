arr = [10, 7, 8, 9, 1, 5]

# NAIVE = O(n^2) worst case, O(n log n) average

def quick_sort_naive(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[-1]
    left = [x for x in nums[:-1] if x <= pivot]
    right = [x for x in nums[:-1] if x > pivot]
    return quick_sort_naive(left) + [pivot] + quick_sort_naive(right)

print(quick_sort_naive(arr))
