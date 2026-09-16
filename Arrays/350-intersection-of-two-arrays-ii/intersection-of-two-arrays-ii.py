class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        frequency = {}
        for num in nums1:
            frequency[num] = frequency.get(num, 0) + 1
        ans = []
        for num in nums2:
            if num in frequency and frequency[num] > 0:
                ans.append(num)
                frequency[num] -= 1
        return ans