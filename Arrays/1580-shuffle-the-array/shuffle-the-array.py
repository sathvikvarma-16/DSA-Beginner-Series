class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1=nums[:n]
        nums2=nums[n:]
        ans=[]
        for i in range(len(nums)//2):
            ans.append(nums1[i])
            ans.append(nums2[i])
        return ans
