# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maximum = float('-inf')  # Store the maximum path sum
        def dfs(node):
            nonlocal maximum
            if node is None:
                return 0
            left = max(0, dfs(node.left))  # Ignore negative left sum
            right = max(0, dfs(node.right))  # Ignore negative right sum

            # Calculate a complete path through the current node.
            total = node.val + left + right  # Path passing through this node
            # We include both branches because the path can go from the left child through the current node to the right child.

            # Save the largest path sum found so far.
            maximum = max(maximum, total)  # Update maximum path sum

            return node.val + max(left, right)  # Return the best single branch to parent
            # We return only one branch to the parent. Why only one branch? Because the parent can extend the path through node 20 using either left or right, but not both. Including both branches would create a split path. not the same path 
            # here we want same path
        dfs(root)
        return maximum


"""
At every node:

Calculate the maximum sum from the left subtree.
Calculate the maximum sum from the right subtree.
Ignore a negative sum because including it would reduce the path sum.
Add the current node's value, left sum, and right sum.
Update the maximum path sum.
Return the current node's value plus the larger of the two branches.
"""
