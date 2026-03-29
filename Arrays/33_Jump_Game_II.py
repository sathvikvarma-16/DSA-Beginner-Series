"""
Problem: Jump Game II
Link: https://leetcode.com/problems/jump-game-ii/

Approach:
- Greedy (level-based / BFS-like).
- Track current jump range [0 → end].
- While traversing, keep updating farthest reachable index.
- When you reach the end of current range → make a jump and extend range.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def jump(nums):
    # Number of jumps
    jumps = 0

    # Current range end and farthest reach
    current_end = 0
    farthest = 0

    # Traverse till second last element
    for i in range(len(nums) - 1):
        # Update farthest reachable index
        farthest = max(farthest, i + nums[i])

        # If we reach the end of current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps
