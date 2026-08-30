# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid # take middle, if middle is bad, then required bad index must be left of it including mid
            else:
                left = mid + 1 # if middle was good, then required index lies on right side of it

        return left
        