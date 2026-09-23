class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)  # Find the first occurrence of ch
        if i == -1:  # If ch is not found
            return word
        prefix = word[:i + 1]  # Take the prefix including ch
        reversed_prefix = prefix[::-1]  # Reverse the prefix
        return reversed_prefix + word[i + 1:]  # Join reversed prefix with remaining part