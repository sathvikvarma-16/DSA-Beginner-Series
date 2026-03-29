"""
Problem: Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/

Approach:
- Use prefix and suffix products.
- First pass: store prefix product in result.
- Second pass: multiply with suffix product.
- Avoid division as required.

Time Complexity: O(n)
Space Complexity: O(1) (excluding output array)
"""

def productExceptSelf(nums):
    n = len(nums)

    # Initialize result array
    result = [1] * n

    # Prefix product pass
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Suffix product pass
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
