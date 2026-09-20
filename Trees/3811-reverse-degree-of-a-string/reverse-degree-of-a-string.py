class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            value = ord('z') - ord(s[i]) + 1
            total += value * (i + 1)
        return total