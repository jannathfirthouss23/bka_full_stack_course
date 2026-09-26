arr = [4, 5, 6, 7, 0, 1, 2]
target = 0

# NAIVE = O(n)

def search_rotated_naive(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

print(search_rotated_naive(arr, target))
