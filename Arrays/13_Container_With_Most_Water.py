"""
Problem: Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/

Approach:
- Use two pointers (left and right).
- Calculate area = min(height[left], height[right]) * width.
- Move the pointer with smaller height inward.
- This maximizes area efficiently.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxArea(height):
    # Initialize two pointers
    left = 0
    right = len(height) - 1

    # Store maximum area
    max_area = 0

    # Traverse while pointers do not meet
    while left < right:
        # Calculate width
        width = right - left

        # Calculate area using smaller height
        current_area = min(height[left], height[right]) * width

        # Update maximum area
        max_area = max(max_area, current_area)

        # Move the pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
