# Given an array and a window size k, slide a window of size k across the array and return the maximum element in each window position.

arr = [1, 3, -1, -3, 5, 3, 6, 7]

#   Window position              Max
#   [1, 3, -1] -3, 5, 3, 6, 7    3
#   1, [3, -1, -3] 5, 3, 6, 7    3
#   1, 3, [-1, -3, 5] 3, 6, 7    5
#   1, 3, -1, [-3, 5, 3] 6, 7    5
#   1, 3, -1, -3, [5, 3, 6] 7    6
#   1, 3, -1, -3, 5, [3, 6, 7]   7

# NAIVE = O(n^k)

def max_sliding_window(nums, k):
    n = len(nums)
    result = []
    for i in range(n - k + 1): # 8 - 3 + 1 = 6
        result.append(max(nums[i : i + k])) # max(arr[2:5])
    return result

print(max_sliding_window(arr, 3))