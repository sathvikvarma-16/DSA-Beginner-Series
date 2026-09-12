from bisect import bisect_right
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))
        arr.sort()
        starts = [x[0] for x in arr]
        # Find next non-overlapping interval
        next_idx = [0] * n
        for i in range(n):
            next_idx[i] = bisect_right(starts, arr[i][1])
        # dp[i][k] = best (score, indices)
        # from i onwards using at most k intervals
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for k in range(1, 5):
                # Option 1: Skip current interval
                skip_score, skip_indices = dp[i + 1][k]
                # Option 2: Take current interval
                j = next_idx[i]
                take_score, take_indices = dp[j][k - 1]
                take_score += arr[i][2]
                take_indices = take_indices + [arr[i][3]]
                # Keep indices sorted for lexicographical comparison
                take_indices.sort()
                # Choose the better option
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)
                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)
                else:
                    # Same score -> lexicographically smaller
                    if take_indices < skip_indices:
                        dp[i][k] = (take_score, take_indices)
                    else:
                        dp[i][k] = (skip_score, skip_indices)
        return dp[0][4][1]