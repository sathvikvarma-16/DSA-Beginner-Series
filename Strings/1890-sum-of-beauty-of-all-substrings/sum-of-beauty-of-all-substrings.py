class Solution:
    def beautySum(self, s: str) -> int:
        total = 0  # Store the sum of beauties
        n = len(s)
        for i in range(n):  # Choose the starting position
            freq = {}  # Store character frequencies
            for j in range(i, n):  # Extend the substring
                ch = s[j]
                freq[ch] = freq.get(ch, 0) + 1  # Increase its frequency
                highest = max(freq.values())  # Highest frequency
                lowest = min(freq.values())  # Lowest non-zero frequency
                total += highest - lowest  # Add this substring's beauty
        return total  # Return the total beauty
