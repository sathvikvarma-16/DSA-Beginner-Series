class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        for num in nums:
            if freq[num]>1:
                return num        