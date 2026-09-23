class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        required = [0] * 26  # Maximum required frequency for each letter
        for word in words2:  # Process every word in words2
            freq = [0] * 26  # Count letters in this word
            for ch in word: 
                freq[ord(ch) - ord('a')] += 1
            for i in range(26):
                required[i] = max(required[i], freq[i])  # Keep the highest requirement
        ans = []
        for word in words1:  # Check every word in words1
            freq = [0] * 26  # Count letters in this word
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            common = True
            for i in range(26):
                if freq[i] < required[i]:  # Not enough of a required letter
                    common = False
                    break
            if common:
                ans.append(word)
        return ans
        
