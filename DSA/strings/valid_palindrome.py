s = "A man, a plan, a canal: Panama"

# NAIVE = O(n)

def valid_palindrome_naive(s):
    cleaned = ""
    for c in s:
        if c.isalnum():
            cleaned += c.lower()
    reversed_str = cleaned[::-1]
    return cleaned == reversed_str

print(valid_palindrome_naive(s))
