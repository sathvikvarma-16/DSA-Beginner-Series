class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        degree = max(frequency.values())
        answer = len(nums)
        for num in frequency:
            if frequency[num] == degree:
                left = 0
                count = 0
                for right in range(len(nums)):
                    if nums[right] == num:
                        count += 1
                    while count == degree:
                        answer = min(answer, right - left + 1)
                        if nums[left] == num:
                            count -= 1
                        left += 1
        return answer