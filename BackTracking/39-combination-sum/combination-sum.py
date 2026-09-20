class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans, sol = [], []  # Store answers and build one combination
        def backtrack(start, total):
            if total == target:  # If the sum reaches the target
                ans.append(sol[:])  # Save a copy of the combination
                return
            if total > target:  # If the sum is too large
                return
            for i in range(start, len(candidates)):  # Try each candidate
                sol.append(candidates[i])  # Choose the number
                backtrack(i, total + candidates[i])  # Use i again to allow reuse
                sol.pop()  # Undo the choice
        backtrack(0, 0)  # Start from index 0 with sum 0
        return ans  # Return all valid combinations

"""
For candidates = [2, 3, 6, 7], target = 7:

Choose 2 → sol = [2], total = 2
    Choose 2 again → sol = [2, 2], total = 4
        Choose 2 again → total = 6
            Choose 2 → total = 8, too large, so return.
        Undo and choose 3 → sol = [2, 2, 3], total = 7 → save it.
    Backtrack and try other choices.
Choose 7 directly → sol = [7], total = 7 → save it.

algo :
Start with an empty combination sol = [] and total = 0.
Choose a candidate and add it to sol.
Add its value to total.
If total == target, save the combination.
If total > target, stop that path.
Call backtrack(i, ...) using the same index i, because we can reuse the number.
Remove the last chosen number using sol.pop().
Try the next candidate.
"""