class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()  # Split the sentence into words
        ans = [""] * len(words)  # Create empty positions for the words
        for word in words:  # Go through each word
            position = int(word[-1]) - 1  # Get its position (index starts at 0)
            ans[position] = word[:-1]  # Put the word in its correct position
        return " ".join(ans)  # Join the words into a sentence
        