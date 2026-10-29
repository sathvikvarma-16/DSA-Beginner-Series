class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def get_mask(ch):
            return 1 << (ord(ch) - ord('a'))

        # Build Euler tour, parent, depth, and root-path XOR masks.
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        base = [0] * n
        timer = 0

        stack = [(0, 0, False)]

        while stack:
            u, p, exiting = stack.pop()

            if exiting:
                tout[u] = timer - 1
                continue

            parent[u] = p
            tin[u] = timer
            timer += 1

            base[u] = (
                (base[p] if u != 0 else 0)
                ^ get_mask(s[u])
            )

            stack.append((u, p, True))

            for v in reversed(graph[u]):
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u, False))

        # Binary lifting table for LCA.
        levels = n.bit_length()
        up = [parent[:]]

        for k in range(1, levels):
            previous = up[k - 1]
            up.append([previous[previous[u]] for u in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for k in range(levels - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        # Fenwick tree supporting range XOR updates
        # and point XOR queries.
        bit = [0] * (n + 2)

        def update(index, value):
            index += 1

            while index < len(bit):
                bit[index] ^= value
                index += index & -index

        def range_update(left, right, value):
            update(left, value)
            update(right + 1, value)

        def point_query(index):
            index += 1
            result = 0

            while index > 0:
                result ^= bit[index]
                index -= index & -index

            return result

        # Process queries.
        chars = list(s)
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]

                delta = get_mask(chars[u]) ^ get_mask(new_char)

                if delta:
                    range_update(tin[u], tout[u], delta)

                chars[u] = new_char

            else:
                u = int(parts[1])
                v = int(parts[2])

                ancestor = lca(u, v)

                mask_u = base[u] ^ point_query(tin[u])
                mask_v = base[v] ^ point_query(tin[v])

                path_mask = (
                    mask_u
                    ^ mask_v
                    ^ get_mask(chars[ancestor])
                )

                # True if at most one bit is set.
                answer.append(
                    path_mask == 0
                    or (path_mask & (path_mask - 1)) == 0
                )

        return answer