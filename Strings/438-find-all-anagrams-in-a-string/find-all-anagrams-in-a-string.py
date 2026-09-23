class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(p) > len(s):
            return ans
        p_count = {}
        window = {}
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1  # Count characters in p
        left = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1  # Add current character
            if right - left + 1 > len(p):  # Keep window size equal to p
                old = s[left]
                window[old] -= 1
                if window[old] == 0:
                    del window[old]
                left += 1
            if window == p_count:  # Same characters with same frequencies
                ans.append(left)
        return ans