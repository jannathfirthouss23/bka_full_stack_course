s = "AABABBA"
k = 1

# NAIVE = O(n^2)

def character_replacement_naive(s, k):
    n = len(s)
    result = 0
    for i in range(n):
        freq = {}
        max_freq = 0
        for j in range(i, n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            max_freq = max(max_freq, freq[s[j]])
            window_len = j - i + 1
            if window_len - max_freq <= k:
                result = max(result, window_len)
            else:
                break
    return result

print(character_replacement_naive(s, k))
