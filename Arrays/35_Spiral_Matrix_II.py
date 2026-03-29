"""
Problem: Spiral Matrix II
Link: https://leetcode.com/problems/spiral-matrix-ii/

Approach:
- Create an n x n matrix initialized with 0.
- Use four boundaries:
    top, bottom, left, right
- Fill numbers from 1 to n^2 in spiral order.
- After each traversal, move boundaries inward.

Time Complexity: O(n^2)
Space Complexity: O(1) (excluding output matrix)
"""

def generateMatrix(n):
    # Create n x n matrix
    matrix = [[0] * n for _ in range(n)]

    # Initialize boundaries
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    num = 1

    # Fill matrix in spiral order
    while top <= bottom and left <= right:
        # Left to right
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        # Top to bottom
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        # Right to left
        for col in range(right, left - 1, -1):
            matrix[bottom][col] = num
            num += 1
        bottom -= 1

        # Bottom to top
        for row in range(bottom, top - 1, -1):
            matrix[row][left] = num
            num += 1
        left += 1

    return matrix
