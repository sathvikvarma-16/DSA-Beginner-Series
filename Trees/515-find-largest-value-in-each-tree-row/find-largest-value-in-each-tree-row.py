# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            largest = float('-inf')  # Store largest value in this level
            for i in range(len(queue)):  # Process current level
                node = queue.popleft()
                largest = max(largest, node.val)  # Update largest value
                if node.left:
                    queue.append(node.left)  # Add left child
                if node.right:
                    queue.append(node.right)  # Add right child
            result.append(largest)  # Store largest value of this level
        return result

"""
Put the root into the queue.
Process all nodes at the current level.
Keep updating largest whenever you find a bigger value.
Add the children of each node to the queue.
After finishing the level, add largest to the result.
Repeat until the queue is empty.
"""