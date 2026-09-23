class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        prefix = s[:k]  # Take the first k characters
        reversed_prefix = prefix[::-1]  # Reverse those characters
        remaining = s[k:]  # Take the characters after the first k
        return reversed_prefix + remaining  # Join both parts

