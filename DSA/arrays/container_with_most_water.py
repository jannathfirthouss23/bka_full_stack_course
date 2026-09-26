# Given an array of heights, each element represents a vertical line on a graph.
# Find two lines that together with form a container that holds the most water.

#       |                   |
#       |                   |~~~~~~~|
#       |   |               |       |
#       |   |       |       |       |
#       |   |       |   |   |       |
#       |   |       |   |   |   |   |
#       |   |   |   |   |   |   |   |
#   |   |   |   |   |   |   |   |   |
#   1   8   6   2   5   4   8   3   7

nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# NAIVE = O(n^2)

def max_area(height):
    best = 0
    n = len(height)
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, (j - i) * min(height[i], height[j]))
    return best

print(max_area(nums))
