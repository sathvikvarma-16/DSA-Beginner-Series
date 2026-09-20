class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []  # Store which group each parenthesis belongs to
        depth = 0  # Track current nesting depth

        for ch in seq:
            if ch == '(':  # Opening parenthesis
                ans.append(depth % 2)  # Assign based on current depth
                depth += 1  # Increase depth
            else:  # Closing parenthesis
                depth -= 1  # Decrease depth first
                ans.append(depth % 2)  # Assign based on matching depth

        return ans  # Return the group assignments