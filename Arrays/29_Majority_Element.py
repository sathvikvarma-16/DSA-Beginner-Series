"""
Problem: Majority Element
Link: https://leetcode.com/problems/majority-element/

Approach:
- Use Boyer-Moore Voting Algorithm.
- Maintain a candidate and count.
- If count becomes 0 → change candidate.
- Increment if same, decrement if different.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        # Choose new candidate when count is zero
        if count == 0:
            candidate = num

        # Increase or decrease count
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate
