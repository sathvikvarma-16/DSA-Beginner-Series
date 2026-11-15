class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even = 1
        odd = 0
        prefix = 0
        result = 0
        for num in arr:
            prefix += num
            if prefix % 2 == 1:
                result += even
                odd += 1
            else:
                result += odd
                even += 1
        return result % MOD
