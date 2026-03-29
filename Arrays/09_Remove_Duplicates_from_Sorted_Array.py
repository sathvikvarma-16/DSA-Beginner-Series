"""
Problem: Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Approach:
- Use two pointers.
- One pointer (j) keeps track of unique elements.
- Traverse array and overwrite duplicates.
- Return length of unique elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def removeDuplicates(nums):
    # Edge case
    if not nums:
        return 0

    # Pointer for unique elements
    j = 0

    # Traverse array
    for i in range(1, len(nums)):
        # If new unique element found
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]

    # Return length of unique elements
    return j + 1
