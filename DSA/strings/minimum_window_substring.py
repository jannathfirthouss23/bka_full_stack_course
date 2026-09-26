s = "ADOBECODEBANC"
t = "ABC"

# NAIVE = O(n^2)

def min_window_naive(s, t):
    if not t or not s:
        return ""
    result = ""
    for i in range(len(s)):
        for j in range(i + len(t), len(s) + 1):
            window = s[i:j]
            if all(window.count(c) >= t.count(c) for c in set(t)):
                if result == "" or len(window) < len(result):
                    result = window
                break
    return result

print(min_window_naive(s, t))
