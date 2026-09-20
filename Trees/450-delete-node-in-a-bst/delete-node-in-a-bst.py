# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:  # If tree is empty
            return None
        if key < root.val:  # Search in left subtree
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:  # Search in right subtree
            root.right = self.deleteNode(root.right, key)
        else:  # Found the node to delete
            if root.left is None:  # No left child
                return root.right
            if root.right is None:  # No right child
                return root.left
            temp = root.right  # Find smallest node in right subtree
            while temp.left:
                temp = temp.left
            root.val = temp.val  # Replace current value with smallest value
            root.right = self.deleteNode(root.right, temp.val)  # Delete duplicate
        return root