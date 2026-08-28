class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        low, high = 0, n1

        while low <= high:

            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1

            l1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            l2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]

            r1 = float("inf") if cut1 == n1 else nums1[cut1]
            r2 = float("inf") if cut2 == n2 else nums2[cut2]

            # Correct partition
            if l1 <= r2 and l2 <= r1:

                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2

                return max(l1, l2)

            # Move left
            elif l1 > r2:
                high = cut1 - 1

            # Move right
            else:
                low = cut1 + 1