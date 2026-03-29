"""
Problem: Minimum Size Subarray Sum
Link: https://leetcode.com/problems/minimum-size-subarray-sum/

Approach:
- Use sliding window.
- Expand right pointer to increase sum.
- Shrink left pointer while sum >= target.
- Track minimum window length.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def minSubArrayLen(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf')

    # Expand window
    for right in range(len(nums)):
        current_sum += nums[right]

        # Shrink window when condition met
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    # If no valid subarray found
    return 0 if min_length == float('inf') else min_length
