"""
Problem: Best Time to Buy and Sell Stock II
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Approach:
- We can complete multiple transactions.
- Whenever there is a profit opportunity (price[i] > price[i-1]),
  we take that profit.
- This works because summing all small profits = maximum profit.

Example:
[7,1,5,3,6,4]
Profit = (5-1) + (6-3) = 4 + 3 = 7

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxProfit(prices):
    # Initialize total profit
    profit = 0

    # Traverse from second element
    for i in range(1, len(prices)):
        # If today's price is greater than yesterday's
        if prices[i] > prices[i - 1]:
            # Add the profit
            profit += prices[i] - prices[i - 1]

    return profit
