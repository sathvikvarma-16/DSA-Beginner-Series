class Solution:
    def makeGood(self, s: str) -> str:
        result = []

        for ch in s:

            if result and abs(ord(result[-1]) - ord(ch)) == 32:
                result.pop()
            else:
                result.append(ch)

        return "".join(result)