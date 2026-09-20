class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans, sol = [], []  # Store answers and build one combination

        def backtrack(start):
            if len(sol) == k:  # If we have chosen k numbers
                ans.append(sol[:])  # Save a copy
                return

            for x in range(start, n + 1):  # Try numbers from start to n
                sol.append(x)  # Choose the number
                backtrack(x + 1)  # Choose the next number after x
                sol.pop()  # Undo the choice

        backtrack(1)  # Start choosing from 1
        return ans  # Return all combinations

"""
Start with number 1.
Add a number to sol.
Call backtrack(x + 1) to choose the next number.
When sol contains k numbers, save a copy in ans.
Remove the last number using sol.pop().
Try the next number.
Return ans.

Why x + 1?
Because we only want each number once, and we want to avoid duplicate combinations like [1, 2] and [2, 1].
"""