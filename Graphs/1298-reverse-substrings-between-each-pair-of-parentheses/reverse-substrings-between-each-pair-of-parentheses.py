class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []  # Store characters
        for ch in s:
            if ch == ')':  # When closing parenthesis appears
                temp = []  # Store characters inside the parentheses
                while stack and stack[-1] != '(':  # Take characters until opening parenthesis
                    temp.append(stack.pop())
                stack.pop()  # Remove the opening parenthesis
                stack.extend(temp)  # Add characters back in reversed order
            else:
                stack.append(ch)  # Add character to the stack
        return "".join(stack)  # Join characters and return the result
        