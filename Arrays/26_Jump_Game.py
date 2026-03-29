  """
Problem: Jump Game
Link: https://leetcode.com/problems/jump-game/

Approach:
- Greedy approach.
- Track the farthest index reachable.
- If current index is beyond reachable → return False.
- Update max reach at each step.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def canJump(nums):
    # Maximum index we can reach
    max_reach = 0

    # Traverse array
    for i in range(len(nums)):
        # If current index is beyond reachable range
        if i > max_reach:
            return False

        # Update maximum reachable index
        max_reach = max(max_reach, i + nums[i])

    return True
