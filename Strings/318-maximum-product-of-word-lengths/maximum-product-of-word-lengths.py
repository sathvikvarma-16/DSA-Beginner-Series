class Solution:
    def maxProduct(self, words: list[str]) -> int:
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                common = False
                for ch in words[i]:
                    if ch in words[j]:
                        common = True
                        break
                if not common:
                    product = len(words[i]) * len(words[j])
                    ans = max(ans, product)
        return ans