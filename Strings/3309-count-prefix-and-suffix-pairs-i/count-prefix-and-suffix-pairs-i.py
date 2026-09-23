class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                word1 = words[i]
                word2 = words[j]
                if word2.startswith(word1) and word2.endswith(word1):
                    count += 1  # Count this valid pair
        return count