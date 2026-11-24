class Solution:
    def maxLength(self, nums: List[int]) -> int:
        from math import gcd
        n = len(nums)
        max_length = 0
        for i in range(n):  # Fix the starting index of the subarray.
            product = 1
            current_gcd = 0
            current_lcm = 1
            for j in range(i, n):  # Extend the subarray one element at a time.
                num = nums[j]
                product *= num  # Update the product of the subarray.
                current_gcd = gcd(current_gcd, num)  # Update GCD.
                current_lcm = (
                    current_lcm * num // gcd(current_lcm, num)
                )  # Update LCM using the GCD-based formula.
                if product == current_gcd * current_lcm:
                    max_length = max(max_length, j - i + 1)
        return max_length