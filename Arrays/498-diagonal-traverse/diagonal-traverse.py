class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)  # Number of rows
        cols = len(mat[0])  # Number of columns
        res = []  # Stores the diagonal traversal result
        cur_row = cur_col = 0  # Start from the top-left cell
        going_up = True  # First diagonal moves upward-right
        while len(res) != rows * cols:  # Continue until every element is visited
            if going_up:  # Move upward-right
                while cur_row >= 0 and cur_col < cols:  # Stay inside top and right boundaries
                    res.append(mat[cur_row][cur_col])  # Add current element to result
                    cur_row -= 1  # Move one row up
                    cur_col += 1  # Move one column right
                if cur_col == cols:  # We went outside through the right boundary
                    cur_col -= 1  # Come back to the last valid column
                    cur_row += 2  # Move to the next starting position
                else:  # We went outside through the top boundary
                    cur_row += 1  # Move down to the next diagonal
                going_up = False  # Change direction to downward-left
            else:  # Move downward-left
                while cur_row < rows and cur_col >= 0:  # Stay inside bottom and left boundaries
                    res.append(mat[cur_row][cur_col])  # Add current element to result
                    cur_col -= 1  # Move one column left
                    cur_row += 1  # Move one row down
                if cur_row == rows:  # We went outside through the bottom boundary
                    cur_col += 2  # Move to the next starting position
                    cur_row -= 1  # Come back to the last valid row
                else:  # We went outside through the left boundary
                    cur_col += 1  # Move right to the next diagonal
                going_up = True  # Change direction to upward-right
        return res  # Return the diagonal traversal