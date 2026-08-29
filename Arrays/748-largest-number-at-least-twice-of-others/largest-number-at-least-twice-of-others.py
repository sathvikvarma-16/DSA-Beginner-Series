class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = float('-inf')
        for i in range(len(nums)):
            largest = max(largest,nums[i])
        index = nums.index(largest)
        for num in nums:
            if num!=largest and largest<2*num:
                return -1
        return index
        