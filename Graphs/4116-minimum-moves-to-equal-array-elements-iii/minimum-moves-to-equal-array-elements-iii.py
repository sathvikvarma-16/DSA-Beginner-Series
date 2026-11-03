class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        total = sum(nums)
        moves = len(nums) * maximum - total
        return moves