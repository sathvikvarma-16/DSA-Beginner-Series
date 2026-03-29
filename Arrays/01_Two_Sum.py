"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Approach:
- Use a hash map (dictionary) to store numbers and their indices.
- For each element, calculate the complement (target - current number).
- If complement exists in the hashmap → return indices.
- Otherwise, store current number with its index.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    # Dictionary to store value -> index
    hashmap = {}

    # Traverse the array
    for i in range(len(nums)):
        # Calculate required complement
        complement = target - nums[i]

        # Check if complement exists in hashmap
        if complement in hashmap:
            # Return indices of complement and current number
            return [hashmap[complement], i]

        # Store current element with its index
        hashmap[nums[i]] = i

    # If no solution found (edge case)
    return []
