"""
Problem: 4Sum
Link: https://leetcode.com/problems/4sum/

Approach:
- Sort the array.
- Fix two elements and use two pointers for remaining two.
- Avoid duplicates carefully.
- Generalization of 3Sum.

Time Complexity: O(n^3)
Space Complexity: O(1) (excluding output)
"""

def fourSum(nums, target):
    # Sort the array
    nums.sort()
    
    result = []
    n = len(nums)

    # First loop
    for i in range(n):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Second loop
        for j in range(i + 1, n):
            # Skip duplicates
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # Two pointers
            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result
