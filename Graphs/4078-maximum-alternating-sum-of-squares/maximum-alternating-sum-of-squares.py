from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        total = 0

        for i in range(n):
            if i < (n + 1) // 2:
                total += nums[n - 1 - i] ** 2
            else:
                total -= nums[i - (n + 1) // 2] ** 2

        return total