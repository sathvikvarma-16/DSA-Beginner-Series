# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def check(node, low, high):
            if node is None:
                return True
            if node.val <= low or node.val >= high:
                return False
            left = check(node.left, low, node.val)  # Left values must be smaller
            right = check(node.right, node.val, high)  # Right values must be greater
            return left and right
        return check(root, float('-inf'), float('inf'))  # Start with unlimited range