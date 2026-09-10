# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.answer = 0

        def dfs(node):
            # Empty subtree
            if node is None:
                return 0, 0

            # Get sum and count from left subtree
            left_sum, left_count = dfs(node.left)

            # Get sum and count from right subtree
            right_sum, right_count = dfs(node.right)

            # Include current node
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            # Calculate average
            average = total_sum // total_count

            # Check if current node equals subtree average
            if node.val == average:
                self.answer += 1

            # Return sum and count to parent
            return total_sum, total_count

        dfs(root)

        return self.answer