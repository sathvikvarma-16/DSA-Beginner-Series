class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(max_sum):
            count = 1
            current = 0
            for num in nums:
                if current + num > max_sum:
                    count += 1
                    current = num
                else:
                    current += num
                if count > k:
                    return False
            return True
        low = max(nums)
        high = sum(nums)
        while low < high:
            mid = (low + high) // 2
            if cansplit(mid):
                high = mid
            else:
                low = mid + 1
        return low