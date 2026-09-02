class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True

"""
If nums1[i] is even, you can keep it as it is, so nums2[i] stays even.
If nums1[i] is odd, you need to subtract another number with the same parity to make it even.
Therefore, if there is at least one even number, every odd number can subtract that even number and remain odd, so that does not help.
To make an odd number even, it must subtract an odd number.
Since j != i, you need another odd number.
"""