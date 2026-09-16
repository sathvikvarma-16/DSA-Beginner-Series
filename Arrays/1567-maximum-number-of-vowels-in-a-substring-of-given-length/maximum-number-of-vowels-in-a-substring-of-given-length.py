class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        max_count = count
        left = 0

        # Slide the window
        for right in range(k, len(s)):

            # Remove left character
            if s[left] in vowels:
                count -= 1

            left += 1

            # Add new right character
            if s[right] in vowels:
                count += 1

            max_count = max(max_count, count)

        return max_count


