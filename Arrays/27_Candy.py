"""
Problem: Candy
Link: https://leetcode.com/problems/candy/

Approach:
- Each child must have at least 1 candy.
- If rating[i] > rating[i-1], give more candies than left.
- If rating[i] > rating[i+1], give more candies than right.
- Use two passes:
    1. Left → Right
    2. Right → Left

Time Complexity: O(n)
Space Complexity: O(n)
"""

def candy(ratings):
    n = len(ratings)

    # Step 1: Give each child at least 1 candy
    candies = [1] * n

    # Step 2: Left to Right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Step 3: Right to Left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # Total candies
    return sum(candies)
