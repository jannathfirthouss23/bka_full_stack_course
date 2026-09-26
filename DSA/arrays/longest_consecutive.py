# Given an unsorted array of integers, find the length of the longest sequence of consecutive numbers.
# Consecutive means numbers that follow each other by exactly 1, like 1, 2, 3, 4 or 100, 101, 102.
# Example,
#   Array: [100, 4, 200, 1, 3, 2]
#   The consecutive sequences present are:
#       1, 2, 3, 4 = length 4
#       100 = length 1
#       200 = length 1

arr = [100, 4, 200, 1, 3, 2]

# NAIVE = O(n^2)

print(set(arr))

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        length = 1
        while num + length in num_set:
            length += 1
        longest = max(longest, length)
    return longest

print(longest_consecutive(arr))