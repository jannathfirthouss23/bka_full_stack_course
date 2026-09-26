arr = [1, 3, 5, 7, 9, 11, 13]
target = 7

# NAIVE = O(n)

def binary_search_naive(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

print(binary_search_naive(arr, target))
