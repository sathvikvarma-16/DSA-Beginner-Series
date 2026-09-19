# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []  # Store all valid paths
        def dfs(node, remaining, path):
            if node is None:
                return  # Stop if node is empty
            path.append(node.val)  # Add current node to path
            remaining -= node.val  # Subtract current value from target
            if node.left is None and node.right is None and remaining == 0:
                result.append(path[:])  # Save a copy of valid path
            dfs(node.left, remaining, path)  # Explore left subtree
            dfs(node.right, remaining, path)  # Explore right subtree
            path.pop()  # Remove current node (backtrack)
        dfs(root, targetSum, [])  # Start from root
        return result  # Return all valid paths



"""
Path Sum II — Quick Dry Run

Tree:

        5
       / \
      4   8
     /   / \
    11  13  4
   / \      / \
  7   2    5   1

Target sum = 22

Step 1: Explore the left path

Follow 5 → 4 → 11 → 7.

Remaining sum: 22 - 5 - 4 - 11 - 7 = -5
Node 7 is a leaf, but the sum is not 22.
Don't save the path. Backtrack.

Next, explore node 2:

5 → 4 → 11 → 2

Remaining sum: 22 - 5 - 4 - 11 - 2 = 0
Node 2 is a leaf, and the remaining sum is 0.
Save [5, 4, 11, 2].
Step 2: Explore the right path

Follow 5 → 8 → 13.

Sum = 5 + 8 + 13 = 26
Not equal to 22. Don't save.

Next, explore 5 → 8 → 4 → 5.

Sum = 5 + 8 + 4 + 5 = 22
Node 5 is a leaf.
Save [5, 8, 4, 5].

Then explore 5 → 8 → 4 → 1.

Sum = 18, not 22.
Don't save.
Final Output
[[5, 4, 11, 2], [5, 8, 4, 5]]
"""

