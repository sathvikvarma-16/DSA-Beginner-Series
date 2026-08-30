class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            # Only start counting at the beginning of a sequence
            if num - 1 not in nums_set:
                current = num
                streak = 1

                while current + 1 in nums_set:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest