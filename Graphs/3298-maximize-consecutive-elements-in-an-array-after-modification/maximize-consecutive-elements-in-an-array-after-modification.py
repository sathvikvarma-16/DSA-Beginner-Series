class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        for num in nums:
            # Option 1: Increase current number by 1
            dp[num + 1] = max(
                dp.get(num + 1, 0),
                dp.get(num, 0) + 1
            )
            # Option 2: Keep current number unchanged
            dp[num] = max(
                dp.get(num, 0),
                dp.get(num - 1, 0) + 1
            )
        return max(dp.values())
