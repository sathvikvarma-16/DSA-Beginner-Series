class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        combined = s + "#" + rev
        lps = [0] * len(combined)
        j = 0
        for i in range(1, len(combined)):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
                lps[i] = j
        return rev[:len(s) - lps[-1]] + s


    
"""
        for i in range(len(s) - 1, -1, -1):
            if s[:i + 1] == s[:i + 1][::-1]:
                remaining = s[i + 1:]
                return remaining[::-1] + s
        return s 
        
        """