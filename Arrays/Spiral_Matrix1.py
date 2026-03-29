"""
Problem: Spiral Matrix
Link: https://leetcode.com/problems/spiral-matrix/

Approach:
- Use four boundaries:
    top, bottom, left, right
- Traverse in this order:
    1. left to right
    2. top to bottom
    3. right to left
    4. bottom to top
- After each traversal, move the corresponding boundary inward.

Time Complexity: O(m * n)
Space Complexity: O(1) (excluding output list)
"""

def spiralOrder(matrix):
    # Result list to store spiral order
    result = []

    # Initialize boundaries
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    # Continue while boundaries are valid
    while top <= bottom and left <= right:
        # Traverse from left to right on top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse from top to bottom on right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse from right to left on bottom row
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse from bottom to top on left column
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
