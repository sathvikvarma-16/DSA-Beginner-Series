# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []  # Empty tree
        result = []  # Store right side view
        queue = deque([root])  # Start with root
        while queue:
            size = len(queue)  # Number of nodes at current level
            for i in range(size):
                node = queue.popleft()  # Remove front node
                if i == size - 1:
                    result.append(node.val)  # Add last node of level
                if node.left:
                    queue.append(node.left)  # Add left child
                if node.right:
                    queue.append(node.right)  # Add right child
        return result  # Return right side view