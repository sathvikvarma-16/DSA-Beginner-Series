# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            total = 0  # Store sum of current level
            size = len(queue)  # Number of nodes in current level
            for i in range(size):
                node = queue.popleft()
                total += node.val  # Add node value
                if node.left:
                    queue.append(node.left)  # Add left child
                if node.right:
                    queue.append(node.right)  # Add right child
            result.append(total / size)  # Calculate and store average
        return result