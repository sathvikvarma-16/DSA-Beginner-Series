class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0  # Current nesting depth
        maximum = 0  # Maximum depth found
        for ch in s:  # Check each character
            if ch == '(':  # Opening parenthesis
                depth += 1  # Increase depth
                maximum = max(maximum, depth)  # Update maximum
            elif ch == ')':  # Closing parenthesis
                depth -= 1  # Decrease depth
        return maximum  # Return the maximum depth