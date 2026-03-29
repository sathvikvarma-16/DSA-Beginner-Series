"""
Problem: Best Time to Buy and Sell Stock IV
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Approach:
- At most k transactions allowed.
- Use dynamic programming:
    buy[i]  -> max profit after i-th buy
    sell[i] -> max profit after i-th sell

- If k >= n/2 → behaves like Stock II (unlimited transactions)

Time Complexity: O(n * k)
Space Complexity: O(k)
"""

def maxProfit(k, prices):
    n = len(prices)
    
    # Edge case
    if n == 0 or k == 0:
        return 0

    # If k is large → treat as unlimited transactions
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    # Initialize DP arrays
    buy = [float('inf')] * (k + 1)
    sell = [0] * (k + 1)

    for price in prices:
        for i in range(1, k + 1):
            # Min cost to buy i-th stock
            buy[i] = min(buy[i], price - sell[i - 1])

            # Max profit after selling i-th stock
            sell[i] = max(sell[i], price - buy[i])

    return sell[k]
