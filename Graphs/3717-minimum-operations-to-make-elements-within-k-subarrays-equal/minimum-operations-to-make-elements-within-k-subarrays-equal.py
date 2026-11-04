from bisect import bisect_left


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, value):
        while i <= self.n:
            self.tree[i] += value
            i += i & -i

    def query(self, i):
        result = 0

        while i > 0:
            result += self.tree[i]
            i -= i & -i

        return result

    def kth(self, k):
        index = 0
        bit = 1 << (self.n.bit_length() - 1)

        while bit:
            nxt = index + bit

            if nxt <= self.n and self.tree[nxt] < k:
                index = nxt
                k -= self.tree[nxt]

            bit >>= 1

        return index + 1


class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)

        # Coordinate compression.
        values = sorted(set(nums))
        m = len(values)

        # Map each number to its compressed index.
        def get_index(num):
            return bisect_left(values, num) + 1

        # Fenwick trees for frequencies and sums.
        counts = Fenwick(m)
        sums = Fenwick(m)

        # Add or remove an element from the current window.
        def update(num, delta):
            idx = get_index(num)
            counts.update(idx, delta)
            sums.update(idx, num * delta)

        # Calculate the cost of making the current window equal.
        def get_cost():
            median_idx = counts.kth((x + 1) // 2)
            median = values[median_idx - 1]

            left_count = counts.query(median_idx)
            left_sum = sums.query(median_idx)

            total_sum = sums.query(m)

            right_count = x - left_count
            right_sum = total_sum - left_sum

            return (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

        # Calculate the minimum cost for every window of size x.
        costs = []

        for i in range(n):
            update(nums[i], 1)

            if i >= x:
                update(nums[i - x], -1)

            if i >= x - 1:
                costs.append(get_cost())

        # DP: minimum cost to select j non-overlapping windows.
        inf = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [inf] * (n + 1)

            for i in range(1, n + 1):
                # Option 1: Skip the current element.
                curr[i] = curr[i - 1]

                # Option 2: Select the window ending at i - 1.
                if i >= x:
                    cost = costs[i - x]

                    curr[i] = min(
                        curr[i],
                        prev[i - x] + cost
                    )

            prev = curr

        return prev[n]