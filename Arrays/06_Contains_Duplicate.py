"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Approach:
- Use a hash set to track seen elements.
- If an element is already in the set → duplicate found.
- Otherwise, add it to the set.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def containsDuplicate(nums):
    # Create an empty set to store seen elements
    seen = set()

    # Traverse through the list
    for num in nums:
        # If number already exists in set → duplicate
        if num in seen:
            return True

        # Add number to set
        seen.add(num)

    # No duplicates found
    return False
