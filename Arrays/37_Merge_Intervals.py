"""
Problem: Merge Intervals
Link: https://leetcode.com/problems/merge-intervals/

Approach:
- Sort intervals based on starting time.
- Traverse and merge overlapping intervals.
- If current interval overlaps with previous, merge them.
- Otherwise, add it as a new interval.

Time Complexity: O(n log n)  (due to sorting)
Space Complexity: O(n)
"""

def merge(intervals):
    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        # If merged list is empty or no overlap
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
