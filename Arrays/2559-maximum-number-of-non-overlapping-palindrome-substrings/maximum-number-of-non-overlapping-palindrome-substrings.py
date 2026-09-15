class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # dp[i] = maximum number of palindromes
        # using the first i characters
        dp = [0] * (n + 1)

        for center in range(n):

            # -------------------------
            # Odd length palindrome
            # -------------------------
            left = center
            right = center

            while left >= 0 and right < n and s[left] == s[right]:

                if right - left + 1 >= k:
                    dp[right + 1] = max(
                        dp[right + 1],
                        dp[left] + 1
                    )
                    break

                left -= 1
                right += 1

            # -------------------------
            # Even length palindrome
            # -------------------------
            left = center
            right = center + 1

            while left >= 0 and right < n and s[left] == s[right]:

                if right - left + 1 >= k:
                    dp[right + 1] = max(
                        dp[right + 1],
                        dp[left] + 1
                    )
                    break

                left -= 1
                right += 1

            # We can also skip this character
            dp[center + 1] = max(
                dp[center + 1],
                dp[center]
            )

        return dp[n]