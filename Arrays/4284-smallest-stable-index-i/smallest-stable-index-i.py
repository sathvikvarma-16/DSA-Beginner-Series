class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        right = [0] * n
        right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right[i] = min(nums[i], right[i + 1])
        max_val = nums[0]
        for i in range(n):
            max_val = max(max_val, nums[i])
            if max_val - right[i] <= k:
                return i
        return -1
    