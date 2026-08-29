class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # Find first smaller element on the left
        left = [-1] * n # stores indices
        for i in range(1, n):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                j = left[j]
            left[i] = j
        # Find first smaller element on the right
        right = [n] * n  # stores indices
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and heights[j] >= heights[i]:
                j = right[j]
            right[i] = j
        # Calculate maximum area
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        return max_area