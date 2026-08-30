class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()  # Step 1: sort the array
        
        closest = nums[0] + nums[1] + nums[2]  # initial closest sum
        
        for i in range(len(nums) - 2):  # fix first number
            
            left = i + 1               # second number
            right = len(nums) - 1      # third number
            
            while left < right:
                
                total = nums[i] + nums[left] + nums[right]
                
                # update closest if this sum is nearer to target
                if abs(target - total) < abs(target - closest):
                    closest = total
                
                # move pointers
                if total < target:
                    left += 1      # need bigger sum
                elif total > target:
                    right -= 1     # need smaller sum
                else:
                    return total   # exact match
        
        return closest
        