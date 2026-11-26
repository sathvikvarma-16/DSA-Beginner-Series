from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Coordinate compression and sentinel
        values = sorted(set(nums))
        mapping = {v: i + 1 for i, v in enumerate(values)}

        s = [mapping[x] for x in nums]
        s.append(0)

        N = n + 1

        # Build suffix array using doubling
        p = list(range(N))
        p.sort(key=lambda i: s[i])

        c = [0] * N

        for i in range(1, N):
            c[p[i]] = c[p[i - 1]] + (
                s[p[i]] != s[p[i - 1]]
            )

        k = 0

        while (1 << k) < N:
            length = 1 << k

            p = [(x - length) % N for x in p]

            count = [0] * N

            for x in c:
                count[x] += 1

            for i in range(1, N):
                count[i] += count[i - 1]

            new_p = [0] * N

            for x in reversed(p):
                count[c[x]] -= 1
                new_p[count[c[x]]] = x

            p = new_p

            new_c = [0] * N

            for i in range(1, N):
                cur = (
                    c[p[i]],
                    c[(p[i] + length) % N]
                )

                prev = (
                    c[p[i - 1]],
                    c[(p[i - 1] + length) % N]
                )

                new_c[p[i]] = (
                    new_c[p[i - 1]] + (cur != prev)
                )

            c = new_c
            k += 1

        # Remove sentinel suffix
        sa = [x for x in p if x != n]

        # Build inverse suffix array
        rank = [0] * n

        for i, pos in enumerate(sa):
            rank[pos] = i

        # Build LCP array using Kasai's algorithm
        lcp = [0] * n
        h = 0

        for i in range(n):
            r = rank[i]

            if r == 0:
                h = 0
                continue

            j = sa[r - 1]

            while (
                i + h < n
                and j + h < n
                and nums[i + h] == nums[j + h]
            ):
                h += 1

            lcp[r] = h

            if h:
                h -= 1

        # Find minimum unique subarray length
        ans = n

        for r, pos in enumerate(sa):
            longest_common = lcp[r]

            if r + 1 < n:
                longest_common = max(
                    longest_common,
                    lcp[r + 1]
                )

            unique_length = longest_common + 1

            # Ensure the subarray fits within nums
            if unique_length <= n - pos:
                ans = min(ans, unique_length)

        return ans