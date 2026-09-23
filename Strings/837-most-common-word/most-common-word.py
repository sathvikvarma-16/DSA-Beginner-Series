class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = {}
        banned_words = set(banned)
        word = ""
        paragraph += " "  # Add space to process the last word
        for ch in paragraph:
            if ch.isalpha():
                word += ch.lower()  # Build the word in lowercase
            elif word:
                if word not in banned_words:
                    words[word] = words.get(word, 0) + 1  # Count the word
                word = ""  # Start building the next word
        ans = ""
        maximum = 0
        for word in words:
            if words[word] > maximum:
                maximum = words[word]
                ans = word
        return ans