class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_i=nums.index(min(nums))
        max_i=nums.index(max(nums))
        left=min(min_i,max_i)
        right=max(min_i,max_i)
        # remove both from left
        option1=right+1
        # remove both from right
        option2 = n-left
        # remove one from left and other from right
        option3 = left+1+n-right
        return min(option1,option2,option3)

