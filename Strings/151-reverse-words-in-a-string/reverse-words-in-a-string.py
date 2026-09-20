class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # Split words and remove extra spaces
        words.reverse()  # Reverse the order of the words
        return " ".join(words)  # Join words with one space