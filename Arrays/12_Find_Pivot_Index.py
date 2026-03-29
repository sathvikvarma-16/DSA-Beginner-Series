"""
Problem: Find Pivot Index
Link: https://leetcode.com/problems/find-pivot-index/

Approach:
- Calculate total sum of array.
- Traverse and maintain left sum.
- Pivot index satisfies:
    left_sum == total_sum - left_sum - current_element

Time Complexity: O(n)
Space Complexity: O(1)
"""

def pivotIndex(nums):
    # Total sum of array
    total_sum = sum(nums)

    # Left sum starts from 0
    left_sum = 0

    # Traverse array
    for i in range(len(nums)):
        # Check pivot condition
        if left_sum == total_sum - left_sum - nums[i]:
            return i

        # Update left sum
        left_sum += nums[i]

    # If no pivot found
    return -1
