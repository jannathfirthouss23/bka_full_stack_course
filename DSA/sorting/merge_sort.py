arr = [38, 27, 43, 3, 9, 82, 10]

# NAIVE = O(n log n)

def merge_sort_naive(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort_naive(nums[:mid])
    right = merge_sort_naive(nums[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort_naive(arr))
