class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # Segment tree
        tree = [[0] * k for _ in range(4 * n)]
        total = [0] * (4 * n)

        def merge(node, left_node, right_node):
            # Product of the complete segment
            total[node] = (total[left_node] * total[right_node]) % k

            # Start with prefixes completely inside the left part
            for r in range(k):
                tree[node][r] = tree[left_node][r]

            # Add prefixes = whole left + prefix of right
            left_product = total[left_node]

            for r in range(k):
                new_r = (left_product * r) % k
                tree[node][new_r] += tree[right_node][r]

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k

                total[node] = rem
                tree[node][rem] = 1

                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node, node * 2, node * 2 + 1)

        def update(node, l, r, index, value):
            if l == r:
                # Clear old information
                for i in range(k):
                    tree[node][i] = 0

                rem = value % k

                total[node] = rem
                tree[node][rem] = 1

                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            merge(node, node * 2, node * 2 + 1)

        def query(node, l, r, ql, qr):
            # Completely outside
            if qr < l or r < ql:
                return None

            # Completely inside
            if ql <= l and r <= qr:
                return total[node], tree[node][:]

            mid = (l + r) // 2

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            if left is None:
                return right

            if right is None:
                return left

            left_total, left_pref = left
            right_total, right_pref = right

            merged_total = (left_total * right_total) % k

            merged_pref = [0] * k

            # Prefixes completely in left
            for r in range(k):
                merged_pref[r] += left_pref[r]

            # Prefixes = whole left + prefix of right
            for r in range(k):
                new_r = (left_total * r) % k
                merged_pref[new_r] += right_pref[r]

            return merged_total, merged_pref

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

            # Persistent update
            update(1, 0, n - 1, index, value)

            # We need prefixes starting from start
            _, pref = query(1, 0, n - 1, start, n - 1)

            ans.append(pref[x])

        return ans