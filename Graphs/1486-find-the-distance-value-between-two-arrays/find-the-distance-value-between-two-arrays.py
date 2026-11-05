from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0

        for num in arr1:
            idx = bisect_left(arr2, num - d)

            if idx == len(arr2) or arr2[idx] > num + d:
                count += 1

        return count