"""
Problem: Best Time to Buy and Sell Stock III
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Approach:
- At most 2 transactions allowed.
- Use 4 variables:
    buy1  -> best cost for first buy
    sell1 -> best profit after first sell
    buy2  -> best cost for second buy (after profit from first)
    sell2 -> best profit after second sell

Logic:
- buy1  = min price so far
- sell1 = max profit after first sell
- buy2  = min effective cost (price - profit1)
- sell2 = max total profit

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxProfit(prices):
    # Edge case
    if not prices:
        return 0

    # Initialize variables
    buy1 = float('inf')
    sell1 = 0
    buy2 = float('inf')
    sell2 = 0

    for price in prices:
        # First buy (min price)
        buy1 = min(buy1, price)

        # First sell (max profit)
        sell1 = max(sell1, price - buy1)

        # Second buy (consider profit from first sell)
        buy2 = min(buy2, price - sell1)

        # Second sell (maximize total profit)
        sell2 = max(sell2, price - buy2)

    return sell2
