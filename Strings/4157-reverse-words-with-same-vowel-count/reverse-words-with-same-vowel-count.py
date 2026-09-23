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