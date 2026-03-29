"""
Problem: Rotate Array
Link: https://leetcode.com/problems/rotate-array/

Approach:
- Reverse method:
    1. Reverse entire array
    2. Reverse first k elements
    3. Reverse remaining elements

- This rotates array to the right by k steps in-place.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def rotate(nums, k):
    n = len(nums)
    
    # Handle k greater than array size
    k = k % n

    # Helper function to reverse part of array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse entire array
    reverse(0, n - 1)

    # Step 2: Reverse first k elements
    reverse(0, k - 1)

    # Step 3: Reverse remaining elements
    reverse(k, n - 1)
