"""
Problem: Maximum Average Subarray I
Link: https://leetcode.com/problems/maximum-average-subarray-i/

Approach:
- Use sliding window of size k.
- Compute sum of first k elements.
- Slide the window one element at a time:
    add next element, remove previous element.
- Track the maximum window sum.
- Final answer = maximum_sum / k

Time Complexity: O(n)
Space Complexity: O(1)
"""

def findMaxAverage(nums, k):
    # Calculate sum of first window of size k
    window_sum = sum(nums[:k])

    # Initialize maximum sum with first window sum
    max_sum = window_sum

    # Slide the window through the array
    for i in range(k, len(nums)):
        # Add new element and remove outgoing element
        window_sum += nums[i] - nums[i - k]

        # Update maximum sum if current window is better
        max_sum = max(max_sum, window_sum)

    # Return maximum average
    return max_sum / k
