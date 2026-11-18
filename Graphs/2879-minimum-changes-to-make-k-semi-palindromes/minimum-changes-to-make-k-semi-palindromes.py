
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # Precompute the cost of making each substring semi-palindromic
        cost = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    group_length = length // d

                    for r in range(d):
                        for t in range(group_length // 2):
                            left = i + r + t * d
                            right = i + r + (group_length - 1 - t) * d

                            if s[left] != s[right]:
                                changes += 1

                    cost[i][j] = min(cost[i][j], changes)

        # DP: minimum changes to divide first i characters into p parts
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
