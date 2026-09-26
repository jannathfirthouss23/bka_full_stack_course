# Given a list of intervals, merge all overlapping intervals and return the result.

arr = [[1, 3], [8, 10], [2, 6], [15, 18]]

# NAIVE = O(n log n)

def merge(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

print(merge(arr))
