# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def height(node):
            if node is None:
                return 0  # Empty subtree has height 0
            left = height(node.left)  
            right = height(node.right)
            if left == -1 or right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return height(root) != -1


"""
1
           / \
          2   3
         /     \
        4       5
       /         \
      6           7
     /
    8

We will calculate the heights from the bottom upward.

Remember:

None returns 0.
If the height difference is greater than 1, return -1.
If a child returns -1, its parent also returns -1.
Step-by-step dry run
Step 1: Node 8

It has no children.

left = 0
right = 0

Difference = 0

Return height = 1.

Step 2: Node 6

Its left child is node 8, and its right child is None.

left = 1
right = 0

Difference = 1

Return height = 1 + max(1, 0) = 2.

Step 3: Node 4

Its left child is node 6, and its right child is None.

left = 2
right = 0

Difference = 2.

Since 2 > 1:

return -1

Node 4 is unbalanced.

Step 4: Node 2

Node 2 receives -1 from its left subtree.

left = -1

The code also calculates its right subtree, which is empty:

right = 0

Now:

if left == -1 or right == -1:
    return -1

Node 2 returns -1.

Step 5: Node 7

Node 7 has no children.

left = 0
right = 0

Difference = 0

Return height = 1.

Step 6: Node 5

Its left child is None, and its right child is node 7.

left = 0
right = 1

Difference = 1

Return height = 2.

Step 7: Node 3

Its left child is None, and its right child is node 5.

left = 0
right = 2

Difference = 2.

Therefore, node 3 also returns -1.

Step 8: Node 1

Node 1 receives:

left = -1
right = -1

Since at least one subtree is unbalanced, it returns -1.

Finally:

return height(root) != -1

Becomes:

return -1 != -1

Final answer: False

The tree is unbalanced.

The most important thing to understand

Notice that node 4 already discovered an imbalance.

That -1 travels upward:

Node 4 returns -1
       ↓
Node 2 returns -1
       ↓
Node 1 returns -1

The right subtree is also checked, but once an unbalanced subtree is found, its ancestors propagate -1.

Remember: A tree must be balanced at every node. Even if the root looks balanced, an unbalanced subtree makes the entire tree unbalanced.
"""