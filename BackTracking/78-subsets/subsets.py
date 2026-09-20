class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans, sol = [], []  # Store all subsets and build one subset
        n = len(nums)

        def backtrack(start):
            ans.append(sol[:])  # Save the current subset

            for i in range(start, n):  # Try each remaining number
                sol.append(nums[i])  # Choose the number
                backtrack(i + 1)  # Continue with the next index
                sol.pop()  # Undo the choice

        backtrack(0)  # Start from index 0
        return ans  # Return all subsets
        