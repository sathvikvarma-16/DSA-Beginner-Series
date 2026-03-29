"""
Problem: Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/

Approach:
- Use two pointers.
- One pointer (j) tracks position to place non-zero elements.
- Traverse array and shift all non-zero elements forward.
- Fill remaining positions with zeroes.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def moveZeroes(nums):
    # Pointer for placing non-zero elements
    j = 0

    # Move all non-zero elements to front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    # Fill remaining positions with zeroes
    for i in range(j, len(nums)):
        nums[i] = 0
