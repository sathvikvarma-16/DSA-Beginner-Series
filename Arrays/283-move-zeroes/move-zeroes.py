class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_position = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[insert_position] = nums[i]
                insert_position += 1

        while insert_position < len(nums):
            nums[insert_position] = 0
            insert_position += 1