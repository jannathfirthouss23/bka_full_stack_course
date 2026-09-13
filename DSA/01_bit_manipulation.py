"""
Bits: ...64 32 16 8 4 2 1
    5 = 101
    3 = 011

AND (&):
      101     (5)
    & 011     (3)
    -------------
      001    = 1

OR (|)
      101     (5)
    | 011     (3)
    -------------
      111    = 7

XOR (^)
      101      (5)
    ^ 011      (3)
    --------------
      110    = 6

NOT (~): -(x + 1)
    ~5 -> -6
    ~0 -> -1

Left shift (<<) - push bits left (adds)
5 << 1:  101 -> 1010   = 10   (5 * 2)
5 << 2:  101 -> 10100  = 20   (5 * 4)

Right shift (>>) - push bits right (removes)
5  >> 1:  101   -> 10      = 2    (5  / 2)
20 >> 2:  10100 -> 101     = 5    (20 / 4)
25 >> 3:  11001 -> 11      = 3
"""

# Given two positive integer n and  k, check if the kth index bit of n is set or not.

def is_kth_bit_set(num, k):
    a = num >> k
    b = a & 1
    return b == 1
    return ((num >> k) & 1) == 1

# ((5 >> k) & 1) == 1

print(is_kth_bit_set(5, 0))
print(is_kth_bit_set(5, 1))

