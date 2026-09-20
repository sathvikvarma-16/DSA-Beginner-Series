class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)  # Make a sorted copy
        count = 0  # Count mismatched positions
        for i in range(len(heights)):  # Check each position
            if heights[i] != expected[i]:  # If heights differ
                count += 1  # Increase the count
        return count  # Return the number of mismatches