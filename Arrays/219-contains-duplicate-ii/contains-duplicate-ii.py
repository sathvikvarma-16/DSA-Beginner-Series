class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexmap = {}
        for i in range(len(nums)):
            if nums[i] in indexmap and i-indexmap[nums[i]]<=k:
                return True
            indexmap[nums[i]]=i
        return False
        