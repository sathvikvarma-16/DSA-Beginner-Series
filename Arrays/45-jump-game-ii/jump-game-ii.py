class Solution:
    def jump(self, nums: List[int]) -> int:
        pointer = len(nums) - 1
        jumps = 0
        while pointer > 0:
            farthest = 0
            for i in range(pointer):
                if i + nums[i] >= pointer:
                    farthest = i
                    break
            pointer = farthest
            jumps += 1
        return jumps
        
    

