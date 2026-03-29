"""
Problem: Set Matrix Zeroes
Link: https://leetcode.com/problems/set-matrix-zeroes/

Approach:
- Use first row and first column as markers.
- First, check separately whether first row or first column originally contains zero.
- For the rest of the matrix:
    if matrix[i][j] == 0, mark matrix[i][0] and matrix[0][j] as 0.
- Then use these markers to set cells to zero.
- Finally, update first row and first column if needed.

Time Complexity: O(m * n)
Space Complexity: O(1)
"""

def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Check if first row contains any zero
    first_row_zero = False
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # Check if first column contains any zero
    first_col_zero = False
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break

    # Use first row and first column as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set cells to zero based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Update first row if needed
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Update first column if needed
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0
