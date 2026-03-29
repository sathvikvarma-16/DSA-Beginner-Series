"""
Problem: Insert Interval
Link: https://leetcode.com/problems/insert-interval/

Approach:
- Add all intervals that end before the new interval starts.
- Merge all overlapping intervals with the new interval.
- Add the merged new interval.
- Add the remaining intervals.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def insert(intervals, newInterval):
    # Result list
    result = []

    i = 0
    n = len(intervals)

    # Step 1: Add all intervals before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Step 2: Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # Add merged interval
    result.append(newInterval)

    # Step 3: Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
