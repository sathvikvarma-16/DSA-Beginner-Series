"""
Problem: 3Sum
Link: https://leetcode.com/problems/3sum/

Approach:
- Sort the array.
- Fix one element and use two pointers to find remaining two elements.
- Avoid duplicates by skipping same values.

Time Complexity: O(n^2)
Space Complexity: O(1) (excluding output)
"""

def threeSum(nums):
    # Sort the array
    nums.sort()
    
    result = []

    # Traverse array
    for i in range(len(nums)):
        # Skip duplicate elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two pointers
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            # Found triplet
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            # Move pointers
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
