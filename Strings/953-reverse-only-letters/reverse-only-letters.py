class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if not ('A' <= s[left] <= 'Z' or 'a' <= s[left] <= 'z'):
                left += 1
            elif not ('A' <= s[right] <= 'Z' or 'a' <= s[right] <= 'z'):
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)

        