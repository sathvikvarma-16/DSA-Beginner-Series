"""
Problem: Trapping Rain Water
Link: https://leetcode.com/problems/trapping-rain-water/

Approach:
- Use two pointers: one from the left and one from the right.
- Keep track of the maximum height seen so far from both sides.
- Water trapped at any position depends on the smaller boundary.
- Move the pointer with the smaller height inward.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def trap(height):
    # Initialize two pointers
    left = 0
    right = len(height) - 1

    # Track maximum heights from both sides
    left_max = 0
    right_max = 0

    # Store total trapped water
    water = 0

    # Traverse until pointers meet
    while left < right:
        # If left height is smaller, process left side
        if height[left] < height[right]:
            # Update left maximum height
            if height[left] >= left_max:
                left_max = height[left]
            else:
                # Water trapped at current position
                water += left_max - height[left]
            left += 1
        else:
            # Update right maximum height
            if height[right] >= right_max:
                right_max = height[right]
            else:
                # Water trapped at current position
                water += right_max - height[right]
            right -= 1

    return water
