class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        result = [0] * len(nums2)
        indexed = sorted(
            [(value, i) for i, value in enumerate(nums2)],reverse=True
        )  # largest to smallest with indices
        # Process the strongest opponent first. If you can beat them, use your biggest number. If you can't, sacrifice your smallest.
        left = 0
        right = len(nums1) - 1
        for value, index in indexed:
            if nums1[right] > value: # Can my biggest remaining number beat this opponent?
            # if yes : use it
                result[index] = nums1[right]
                right -= 1
            else:
                # otherwise sacrifice the smallest
                result[index] = nums1[left]
                left += 1
        return result
