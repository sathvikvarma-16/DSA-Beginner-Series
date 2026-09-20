class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []  # Track opening parentheses
        ans = ""  # Store the result
        for ch in s:  # Go through each character
            if ch == '(':  # If opening parenthesis
                if stack:  # If already inside a group
                    ans += ch  # Keep this parenthesis
                stack.append(ch)  # Push opening parenthesis
            else:  # If closing parenthesis
                stack.pop()  # Remove matching opening parenthesis
                if stack:  # If still inside the group
                    ans += ch  # Keep this parenthesis
        return ans  # Return the result
    
"""
When ( appears:
If the stack is not empty, keep it.
Push ( onto the stack.
When ) appears:
Pop one ( from the stack.
If the stack is not empty, keep ).
If the stack is empty, that parenthesis was an outermost one, so skip it.
"""
