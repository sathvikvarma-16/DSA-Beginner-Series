"""
Problem: Plus One
Link: https://leetcode.com/problems/plus-one/

Approach:
- Traverse the digits from right to left.
- If digit is less than 9 → add 1 and return.
- If digit is 9 → make it 0 and carry forward.
- If all digits are 9 → add new leading 1.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def plusOne(digits):
    # Traverse from last digit
    for i in range(len(digits) - 1, -1, -1):
        # If digit is less than 9 → just add 1
        if digits[i] < 9:
            digits[i] += 1
            return digits

        # If digit is 9 → set to 0 and continue
        digits[i] = 0

    # If all digits were 9 → add leading 1
    return [1] + digits
