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
        