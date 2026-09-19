"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        queue = deque([root])  # Add root to queue
        while queue:
            size = len(queue)  # Number of nodes in current level
            for i in range(size):
                node = queue.popleft()  # Remove current node
                if i < size - 1: # If the current node isn't the last node of its level, connect it to the next node waiting in the queue.
                    node.next = queue[0]  # Connect to next node in same level
                if node.left:
                    queue.append(node.left)  # Add left child
                if node.right:
                    queue.append(node.right)  # Add right child
        return root

"""
Add the root to the queue.
Process all nodes at the current level.
Connect each node to the next node in the queue, except the last node.
Add the left and right children to the queue.
Repeat for every level.
Return the root.
"""