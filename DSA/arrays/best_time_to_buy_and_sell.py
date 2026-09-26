# Given an array where each element represents the stock price on that day.
# Can buy once and sell once. Find the maximum profit.

nums = [7, 1, 5, 3, 6, 4]

# NAIVE = O(n^2)

def max_profit(prices):
    best = 0 # 5
    n = len(prices)
    for buy in range(n):
        for sell in range(buy + 1, n):
            # if (prices[sell] - prices[buy]) > best:
            #     best = prices[sell] - prices[buy]
            best = max(best, prices[sell] - prices[buy])
    return best

print(max_profit(nums))