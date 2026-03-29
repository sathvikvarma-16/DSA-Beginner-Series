"""
Problem: Find All Numbers Disappeared in an Array
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Approach:
- Use index marking technique.
- For each number x, mark index abs(x)-1 as negative.
- After marking, the indices that remain positive are missing numbers.

Time Complexity: O(n)
Space Complexity: O(1) (excluding output)
"""

def findDisappearedNumbers(nums):
    # Mark indices as visited
    for num in nums:
        index = abs(num) - 1

        # Make value at index negative to mark presence
        if nums[index] > 0:
            nums[index] = -nums[index]

    # Collect indices that are still positive
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i + 1)

    return result
