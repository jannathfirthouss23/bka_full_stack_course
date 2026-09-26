s = "abcabcbb"

# NAIVE = O(n^2)

def longest_substring_naive(s):
    n = len(s)
    result = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            result = max(result, j - i + 1)
    return result

print(longest_substring_naive(s))
