class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        vowels = "aeiou"
        count = 0
        for ch in words[0]:
            if ch in vowels:
                count += 1
        for i in range(1, len(words)):
            vowel_count = 0
            for ch in words[i]:
                if ch in vowels:
                    vowel_count += 1
            if vowel_count == count:
                words[i] = words[i][::-1]
        return " ".join(words)
    
"""
You are given a sentence containing multiple words.

Count the number of vowels in the first word.
Keep the first word unchanged.
For every other word:
Count its vowels.
If its vowel count is equal to the first word's vowel count, reverse that word.
Otherwise, leave it unchanged.
Return the sentence with the words joined by spaces.
"""