class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort()  # Sort alphabetically
        word_set = set(words)
        valid = set()  # Store words that can be built
        ans = ""
        for word in words:
            if len(word) == 1 or word[:-1] in valid:
                valid.add(word)  # This word can be built
                if len(word) > len(ans):
                    ans = word  # Update the longest word
        return ans
"""
What is the problem asking?

You are given a list of words.

You need to find the longest word that can be built one character at a time, where every shorter prefix of that word must also exist in the list.

Example 1
words = ["w", "wo", "wor", "worl", "world"]

We can build the word step by step:

"w" → "wo" → "wor" → "worl" → "world"

Every step exists in the list, so "world" is valid.

Output:

"world"
Example 2
words = ["a", "banana", "app", "ap", "appl", "apply", "apple"]
"apple" is valid because "a", "ap", "app", and "appl" exist.
"apply" is also valid because "a", "ap", "app", and "appl" exist.
Both have length 5.
When words have the same maximum length, choose the lexicographically smaller word.

Output:

"apple"
Remember
Every prefix must exist in the dictionary.
Find the longest word satisfying that condition.
If there is a tie, return the lexicographically smallest word.
If no valid word exists, return "".
"""