class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans, sol = [], []  # ans stores answers; sol builds one permutation
        nums.sort()  # Put duplicate numbers next to each other
        n = len(nums)
        used = [False] * n  # Track which positions we have chosen
        def backtrack():
            if len(sol) == n:  # If all numbers are chosen
                ans.append(sol[:])  # Save a copy of this permutation
                return
            for i in range(n):  # Try every position
                if used[i]:  # Skip a number already chosen
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue  # Skip duplicate choice to avoid repeated permutations
                sol.append(nums[i])  # Choose this number
                used[i] = True  # Mark its position as used
                backtrack()  # Explore the next position
                sol.pop()  # Undo the choice
                used[i] = False  # Mark its position as unused
        backtrack()
        return ans