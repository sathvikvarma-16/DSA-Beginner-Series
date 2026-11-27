
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Step 1: Calculate free copies for each item
        free = [0] * n

        for i in range(n):
            factor = items[i][0]

            for j in range(n):
                if i != j and items[j][0] % factor == 0:
                    free[i] += 1

        # Step 2: Knapsack DP
        # dp[b] = maximum copies obtainable with spending exactly b
        dp = [0] + [-1] * budget

        for i in range(n):
            price = items[i][1]
            bonus = free[i]

            new_dp = dp[:]

            # Group spending amounts by remainder modulo price
            for r in range(min(price, budget + 1)):
                best = float("-inf")

                max_m = (budget - r) // price

                for m in range(1, max_m + 1):
                    q = m - 1
                    previous_cost = r + q * price

                    if dp[previous_cost] != -1:
                        best = max(best, dp[previous_cost] - q)

                    current_cost = r + m * price

                    if best != float("-inf"):
                        candidate = m + bonus + best

                        new_dp[current_cost] = max(
                            new_dp[current_cost],
                            candidate
                        )

            dp = new_dp

        return max(dp)
