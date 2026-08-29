class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        # Find the first number from the right that is smaller than the next number
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # If such a number exists, find a bigger number from the right
        if i >= 0: # We now need to find a number just bigger than nums[i] from the right side.
            j = n - 1
            while nums[j] <= nums[i]: 
                j -= 1
            # Swap them to make the permutation slightly bigger
            nums[i], nums[j] = nums[j], nums[i]
        # Reverse the right side to make it as small as possible
        nums[i + 1:] = reversed(nums[i + 1:])
