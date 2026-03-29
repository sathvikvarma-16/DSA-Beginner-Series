"""
Problem: Maximum Product Subarray
Link: https://leetcode.com/problems/maximum-product-subarray/

Approach:
- Track both current maximum and current minimum.
- Negative numbers can flip max ↔ min.
- At each step:
    current_max = max(num, num * prev_max, num * prev_min)
    current_min = min(num, num * prev_max, num * prev_min)
- Update global maximum.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxProduct(nums):
    # Initialize current max, current min, and global max
    current_max = nums[0]
    current_min = nums[0]
    max_product = nums[0]

    # Traverse from second element
    for i in range(1, len(nums)):
        num = nums[i]

        # Store previous max before updating
        temp_max = current_max

        # Update current max and min
        current_max = max(num, num * current_max, num * current_min)
        current_min = min(num, num * temp_max, num * current_min)

        # Update global maximum product
        max_product = max(max_product, current_max)

    return max_product
