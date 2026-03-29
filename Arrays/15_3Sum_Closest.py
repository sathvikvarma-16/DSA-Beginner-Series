"""
Problem: 3Sum Closest
Link: https://leetcode.com/problems/3sum-closest/

Approach:
- Sort the array.
- Fix one element and use two pointers to find closest sum.
- Track the closest sum using absolute difference.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def threeSumClosest(nums, target):
    # Sort the array
    nums.sort()
    
    # Initialize closest sum with first three elements
    closest_sum = nums[0] + nums[1] + nums[2]

    # Traverse array
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # Update closest sum if better
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            # Move pointers
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # Exact match
                return current_sum

    return closest_sum
