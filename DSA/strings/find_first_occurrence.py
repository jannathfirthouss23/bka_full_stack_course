haystack = "sadbutsad"
needle = "sad"

# NAIVE = O(n * m)

def find_first_occurrence_naive(haystack, needle):
    n = len(haystack)
    m = len(needle)
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    return -1

print(find_first_occurrence_naive(haystack, needle))
