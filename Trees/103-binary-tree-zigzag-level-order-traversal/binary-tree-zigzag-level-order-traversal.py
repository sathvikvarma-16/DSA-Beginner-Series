# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        left_to_right = True
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()  # Reverse alternate levels
            result.append(level)
            left_to_right = not left_to_right  # Change direction
        return result

"""
Return the nodes level by level, but alternate the direction at each level.

Level 1 → Left to Right
Level 2 → Right to Left
Level 3 → Left to Right
Level 4 → Right to Left
"""


"""
Example Tree
                  1
                /   \
               2     3
              / \   / \
             4   5 6   7
            / \   \    / \
           8   9  10  11 12
          /       / \
         13      14 15

Expected output:

[
    [1],
    [3, 2],
    [4, 5, 6, 7],
    [12, 11, 10, 9, 8],
    [13, 14, 15]
]
Initial Values
result = []
queue = deque([root])
left_to_right = True

Initially:

result = []

queue = [1]

left_to_right = True

Since left_to_right = True, the first level will be processed from left to right.

Step 1: Process Level 1

Current queue:

[1]

We take node 1.

level.append(1)

Node 1 has children 2 and 3, so add them to the queue.

queue = [2, 3]
level = [1]

Since left_to_right = True, we don't reverse.

Add the level to the result:

result = [[1]]

Change direction:

left_to_right = not left_to_right

Now:

left_to_right = False
Step 2: Process Level 2

Current queue:

[2, 3]

We process 2:

Add 2 to the level.
Add its children 4 and 5 to the queue.

We process 3:

Add 3 to the level.
Add its children 6 and 7 to the queue.

Now:

level = [2, 3]

queue = [4, 5, 6, 7]

Since left_to_right = False, reverse the level.

level.reverse()

Now:

level = [3, 2]

Add it to the result:

result = [[1], [3, 2]]

Change direction:

left_to_right = True
Step 3: Process Level 3

Current queue:

[4, 5, 6, 7]

Process each node:

Node	Children added to queue
4	8, 9
5	10
6	None
7	11, 12

The level becomes:

level = [4, 5, 6, 7]

The queue becomes:

queue = [8, 9, 10, 11, 12]

Since left_to_right = True, we don't reverse.

Add the level:

result = [[1], [3, 2], [4, 5, 6, 7]]

Change direction:

left_to_right = False
Step 4: Process Level 4

Current queue:

[8, 9, 10, 11, 12]

Process each node:

Node	Children added to queue
8	13
9	None
10	14, 15
11	None
12	None

The level becomes:

level = [8, 9, 10, 11, 12]

The queue becomes:

queue = [13, 14, 15]

Since left_to_right = False, reverse the level.

level.reverse()

Now:

level = [12, 11, 10, 9, 8]

Add it to the result:

result = [
    [1],
    [3, 2],
    [4, 5, 6, 7],
    [12, 11, 10, 9, 8]
]

Change direction:

left_to_right = True
Step 5: Process Level 5

Current queue:

[13, 14, 15]

All three nodes are leaf nodes.

Process them:

level = [13, 14, 15]

No children are added.

queue = []

Since left_to_right = True, we don't reverse.

Add the level:

result = [
    [1],
    [3, 2],
    [4, 5, 6, 7],
    [12, 11, 10, 9, 8],
    [13, 14, 15]
]

The queue is empty, so the while loop stops.
"""