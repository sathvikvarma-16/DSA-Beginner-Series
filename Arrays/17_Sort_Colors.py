"""
Problem: Sort Colors
Link: https://leetcode.com/problems/sort-colors/

Approach:
- Use Dutch National Flag algorithm.
- Maintain three pointers:
    low  -> boundary for 0s
    mid  -> current index
    high -> boundary for 2s

- Traverse and swap elements into correct regions.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def sortColors(nums):
    # Initialize pointers
    low = 0
    mid = 0
    high = len(nums) - 1

    # Traverse array
    while mid <= high:
        # Case 0 → swap with low
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        # Case 1 → move forward
        elif nums[mid] == 1:
            mid += 1

        # Case 2 → swap with high
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
