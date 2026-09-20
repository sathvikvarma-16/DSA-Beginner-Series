class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []  # Stores all completed permutations
        sol = []  # Stores the permutation we are currently building
        n = len(nums)  # Number of elements needed in each permutation

        def backtrack():
            # BASE CASE: If sol contains all numbers, the permutation is complete
            if len(sol) == n:
                ans.append(sol[:])  # Save a COPY of the current permutation
                return  # Finish this call and go back to the call that made it

            # Try every number in nums
            for x in nums:
                if x not in sol:  # Only choose a number that is not already used
                    sol.append(x)  # CHOOSE: Add this number to the current permutation

                    backtrack()  # EXPLORE: Start a new call to choose the next number
                    # This call pauses here until the deeper call finishes

                    sol.pop()  # UNDO: Remove the number this call added
                    # Now this call can continue its loop and try another number

        backtrack()  # Start building permutations
        return ans  # Return all completed permutations

    
"""
Call 1 adds 1
    Call 2 adds 2
        Call 3 adds 3
            Call 4 saves [1, 2, 3] and returns
        Call 3 resumes and removes 3
        Call 3 finishes and returns
    Call 2 resumes and removes 2
    Call 2 adds 3
        Call 5 adds 2
            Call 6 saves [1, 3, 2] and returns
        Call 5 resumes and removes 2
        Call 5 finishes and returns
    Call 2 resumes and removes 3
    Call 2 finishes and returns
Call 1 resumes and removes 1
Call 1 tries 2 and explores [2, 1, 3] and [2, 3, 1]
Call 1 resumes and removes 2
Call 1 tries 3 and explores [3, 1, 2] and [3, 2, 1]
Call 1 resumes and removes 3
Call 1 finishes
"""

