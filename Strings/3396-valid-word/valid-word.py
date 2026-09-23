class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:  # Word must contain at least 3 characters
            return False
        vowels = "aeiouAEIOU"
        has_vowel = False
        has_consonant = False
        for ch in word:
            if not ch.isalnum():  # Reject special characters
                return False
            if ch.isalpha():  # Check only English letters for vowel/consonant
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
        return has_vowel and has_consonant  # Both must be present
        