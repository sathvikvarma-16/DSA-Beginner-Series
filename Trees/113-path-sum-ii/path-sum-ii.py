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