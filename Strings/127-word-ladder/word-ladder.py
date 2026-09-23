from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)  # Store words in a set for fast checking
        if endWord not in words:  # If the ending word is unavailable
            return 0
        queue = deque([(beginWord, 1)])  # Store the word and sequence length => queue = [("hit", 1)] => This means we are starting at "hit", and the sequence length is 1.
        words.discard(beginWord)  # This removes "hit" from the set if it is present.
        while queue:
            word, steps = queue.popleft()  # Take the next word and its length
            if word == endWord:  # If we reached the target
                return steps
            for i in range(len(word)):  # Try changing each character
                for ch in "abcdefghijklmnopqrstuvwxyz":  # Try every lowercase letter
                    newWord = word[:i] + ch + word[i + 1:]  # Create a new word
                    if newWord in words:  # Continue only if it is allowed and unvisited
                        words.remove(newWord)  # Mark it as visited 
                        queue.append((newWord, steps + 1))  # Add it to the queue
        return 0  # No valid transformation exists



"""
1. Understand the problem simply

You are given:

beginWord — the word where you start.
endWord — the word you want to reach.
wordList — the list of words you are allowed to use.

Your task: Find the shortest number of words in a transformation sequence from beginWord to endWord.

Rules
You can change only one letter at a time.
Every new word must be present in wordList.
The final word must be endWord.
Count both the starting word and the ending word.
If you cannot reach endWord, return 0.
Example
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
One possible transformation is:
hit → hot → dot → dog → cog
Each step changes only one letter.
There are 5 words in this sequence, so the answer is 5.
Another possible sequence is:
hit → hot → lot → log → cog
It also contains 5 words.
We need the shortest sequence, so we use BFS (Breadth-First Search).
"""