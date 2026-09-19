# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if subRoot is None:
            return True  # Empty tree is a subtree
        if root is None:
            return False  # Main tree is empty
        if self.isSame(root, subRoot):
            return True  # Trees match completely
        left = self.isSubtree(root.left, subRoot)  # Search left subtree
        right = self.isSubtree(root.right, subRoot)  # Search right subtree
        return left or right  # True if found on either side
    def isSame(self, a, b):
        if a is None and b is None:
            return True  # Both nodes are empty
        if a is None or b is None:
            return False  # Only one node is empty
        if a.val != b.val:
            return False  # Values do not match
        return self.isSame(a.left, b.left) and self.isSame(a.right, b.right)  # Check both sides


"""
Same indentation level → Call using self.isSame().
Inside isSubtree() → Call it directly as isSame().
Here, self refers to the current Solution object.
""" 