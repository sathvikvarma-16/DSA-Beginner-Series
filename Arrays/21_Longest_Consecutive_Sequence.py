"""
Problem: Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Approach:
- Use a hash set for O(1) lookups.
- Only start counting when num-1 is NOT present (start of sequence).
- Expand forward (num+1, num+2, ...) to count sequence length.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def longestConsecutive(nums):
    # Convert list to set for fast lookup
    num_set = set(nums)

    longest_streak = 0

    for num in num_set:
        # Start only if it's the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Expand the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update longest streak
            longest_streak = max(longest_streak, current_streak)

    return longest_streak
