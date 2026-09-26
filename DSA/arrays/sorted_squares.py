# Given a sorted array (can have negatives), return a new array of the squares of each element, also in sorted order.

arr = [-4, -1, 0, 3, 10]

# NAIVE = O(n log n)

def sorted_squares(nums):
    squares = [x * x for x in nums]
    squares.sort()
    return squares

print(sorted_squares(arr))