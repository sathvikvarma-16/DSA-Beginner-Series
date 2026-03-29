"""
Problem: Search in Rotated Sorted Array
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

Approach:
- Use binary search.
- In every step, one half will always be sorted.
- Check whether target lies in the sorted half.
- Move left or right accordingly.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Target found
        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
