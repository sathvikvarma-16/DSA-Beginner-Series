class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):  # No zigzag needed
            return s
        rows = [""] * numRows  # Create a string for each row
        currentRow = 0  # Start at the first row
        direction = 1  # 1 means down, -1 means up
        for char in s:  # Go through each character
            rows[currentRow] += char  # Add character to current row
            if currentRow == 0:  # If at the top
                direction = 1  # Move down
            elif currentRow == numRows - 1:  # If at the bottom
                direction = -1  # Move up
            currentRow += direction  # Move to the next row
        return "".join(rows)  # Join rows to get the answer
        