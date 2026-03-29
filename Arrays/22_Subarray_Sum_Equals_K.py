"""
Problem: Subarray Sum Equals K
Link: https://leetcode.com/problems/subarray-sum-equals-k/

Approach:
- Use prefix sum + hashmap.
- Store frequency of prefix sums.
- If (current_sum - k) exists → valid subarray found.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def subarraySum(nums, k):
    # Dictionary to store prefix sum frequencies
    prefix_map = {0: 1}

    current_sum = 0
    count = 0

    # Traverse array
    for num in nums:
        current_sum += num

        # Check if there exists a prefix with sum = current_sum - k
        if current_sum - k in prefix_map:
            count += prefix_map[current_sum - k]

        # Store/update current prefix sum
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

    return count
