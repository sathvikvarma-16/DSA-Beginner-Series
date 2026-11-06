from collections import defaultdict
class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )
        active = defaultdict(int)
        ans = [0] * len(queries)
        left = 0
        right = 0
        m = len(logs)
        for q, idx in sorted_queries:
            start = q - x
            # Add requests within the current time window.
            while right < m and logs[right][1] <= q:
                active[logs[right][0]] += 1
                right += 1
            # Remove requests older than the current window.
            while left < right and logs[left][1] < start:
                server_id = logs[left][0]
                active[server_id] -= 1
                if active[server_id] == 0:
                    del active[server_id]
                left += 1
            # Count servers without active requests.
            ans[idx] = n - len(active)
        return ans