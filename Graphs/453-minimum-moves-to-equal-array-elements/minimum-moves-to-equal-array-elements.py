class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimum = min(nums)
        total = sum(nums)
        moves = total - len(nums) * minimum
        return moves