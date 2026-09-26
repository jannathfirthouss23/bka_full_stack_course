# Same as Maximum Subarray, but now the array is circular - the end connects back to the beginning.

arr = [5, -3, 5]

# NAIVE = O(n^2)

def max_subarray_sum_circular(nums):
    n = len(nums)
    best = float("-inf")
    for start in range(n):
        running = 0
        for length in range(1, n + 1):
            running += nums[(start + length - 1) % n]
            best = max(best, running)
    return best

print(max_subarray_sum_circular(arr))