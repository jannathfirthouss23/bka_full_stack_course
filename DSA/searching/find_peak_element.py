arr = [1, 2, 3, 1]

# NAIVE = O(n)

def find_peak_naive(nums):
    n = len(nums)
    for i in range(n):
        left = nums[i] > nums[i - 1] if i > 0 else True
        right = nums[i] > nums[i + 1] if i < n - 1 else True
        if left and right:
            return i
    return -1

print(find_peak_naive(arr))
