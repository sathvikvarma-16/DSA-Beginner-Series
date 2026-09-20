class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans, sol = [], []  # Store all subsets and build one subset
        nums.sort()  # Put duplicate numbers next to each other
        n = len(nums)

        def backtrack(start):
            ans.append(sol[:])  # Save the current subset

            for i in range(start, n):  # Try each remaining number
                if i > start and nums[i] == nums[i - 1]:  # Skip duplicate choices at this level
                    continue

                sol.append(nums[i])  # Choose the number
                backtrack(i + 1)  # Continue from the next index
                sol.pop()  # Undo the choice

        backtrack(0)  # Start from index 0
        return ans  # Return all unique subsets