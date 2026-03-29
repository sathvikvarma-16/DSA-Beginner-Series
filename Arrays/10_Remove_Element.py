"""
Problem: Remove Element
Link: https://leetcode.com/problems/remove-element/

Approach:
- Use two pointers.
- Pointer j tracks position to place elements not equal to val.
- Traverse array and overwrite elements equal to val.
- Return new length of array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def removeElement(nums, val):
    # Pointer for placing valid elements
    j = 0

    # Traverse array
    for i in range(len(nums)):
        # If element is not equal to val
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1

    # Return new length
    return j
