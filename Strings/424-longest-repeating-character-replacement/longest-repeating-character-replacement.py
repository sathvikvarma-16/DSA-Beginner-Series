class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Store frequency of each character
        left = 0
        maximum = 0
        ans = 0
        for right in range(len(s)):
            ch = s[right]
            count[ch] = count.get(ch, 0) + 1  # Count current character
            maximum = max(maximum, count[ch])  # Highest frequency in window
            while (right - left + 1) - maximum > k:  # Too many changes needed
                count[s[left]] -= 1
                left += 1  # Shrink window from the left
            ans = max(ans, right - left + 1)  # Update longest valid length
        return ans