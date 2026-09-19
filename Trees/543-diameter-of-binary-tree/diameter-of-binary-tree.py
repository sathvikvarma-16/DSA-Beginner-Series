# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0  # Store the maximum diameter
        def height(node):
            nonlocal diameter  # Allow us to update diameter
            if node is None:
                return 0  # Empty tree has height 0
            left = height(node.left)  # Find left subtree height
            right = height(node.right)  # Find right subtree height
            diameter = max(diameter, left + right)  # Update diameter
            return 1 + max(left, right)  # Return current height
        height(root)  # Calculate heights and update diameter
        return diameter  # Return the longest path in edges


# In our code, we return height as the number of nodes instead of edges. so that we are doing +1