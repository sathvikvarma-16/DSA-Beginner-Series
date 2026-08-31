class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # If word2 is empty, delete all remaining characters of word1
        for i in range(m + 1):
            dp[i][n] = m - i

        # If word1 is empty, insert all remaining characters of word2
        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):

            for j in range(n - 1, -1, -1):

                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]

                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],      # Delete
                        dp[i][j + 1],      # Insert
                        dp[i + 1][j + 1]   # Replace
                    )

        return dp[0][0]