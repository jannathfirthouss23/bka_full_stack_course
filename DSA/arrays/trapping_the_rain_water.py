# Given an array of heights (like buildings/bars), find how much water gets trapped between them after it rains.

#   Index:      0   1   2   3   4   5
#   Heights:    4   2   0   3   2   5
#   Max Left:   4   4   4   4   4   5
#   Max Right:  5   5   5   5   5   5

nums = [4,2,0,3,2,5]

# NAIVE = O(n)

# MAX LEFT
# i = 0, [:i+1] = 4
# i = 1, [:i+1] = 4
# i = 2, [:i+1] = 4
# i = 3, [:i+1] = 4
# i = 4, [:i+1] = 4
# i = 5, [:i+1] = 5

# MAX RIGHT
# i = 0, [i:] = 5
# i = 1, [i:] = 5
# i = 2, [i:] = 5
# i = 3, [i:] = 5
# i = 4, [i:] = 5
# i = 5, [i:] = 5

# TOTAL

# i = 0, 4 - 4 = 0
# i = 1, 4 - 2 = 2
# i = 2, 4 - 0 = 4
# i = 3, 4 - 3 = 1
# i = 4, 4 - 2 = 2
# i = 5, 5 - 5 = 0

def trap(height):
    total = 0 # 0
    n = len(height) # 6
    for i in range(n):
        left_max = max(height[:i + 1])
        right_max = max(height[i:])
        result = min(left_max, right_max) - height[i]
        total += result
    return total

print(trap(nums))