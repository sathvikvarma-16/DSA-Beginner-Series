"""
Problem: Find Minimum in Rotated Sorted Array
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Approach:
- Use binary search.
- Compare mid with right element:
    → If nums[mid] > nums[right] → minimum is in right half
    → Else → minimum is in left half (including mid)
- Continue until left == right.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Minimum lies in right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Minimum lies in left half (including mid)
            right = mid

    return nums[left]
