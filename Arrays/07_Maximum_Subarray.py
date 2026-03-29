"""
Problem: Maximum Subarray
Link: https://leetcode.com/problems/maximum-subarray/

Approach:
- Use Kadane’s Algorithm.
- At each index, decide:
    → Extend current subarray OR start new subarray
- Track maximum sum seen so far.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxSubArray(nums):
    # Initialize current sum and maximum sum
    current_sum = nums[0]
    max_sum = nums[0]

    # Traverse from second element
    for i in range(1, len(nums)):
        # Either extend previous subarray or start new
        current_sum = max(nums[i], current_sum + nums[i])

        # Update maximum sum found so far
        max_sum = max(max_sum, current_sum)

    return max_sum
