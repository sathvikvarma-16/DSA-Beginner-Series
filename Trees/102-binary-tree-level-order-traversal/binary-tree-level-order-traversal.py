# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        result = []
        queue = deque([root]) # It creates a queue containing the root node 
        # means we put the root node inside the queue.
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft() # Remove front node
                level.append(node.val) # Add its value to level 
                if node.left:
                    queue.append(node.left) # Add left child to queue
                if node.right:
                    queue.append(node.right)  # Add right child to queue
            result.append(level) # Store completed level
        return result

