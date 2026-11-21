class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        # Build the original tree
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        # Store the new parent of every node
        new_parent = parent[:]
        # Track the nearest ancestor having each character
        last = {}
        # First DFS: Find new parents using the original tree
        stack = [(0, False, None)]
        while stack:
            node, exiting, previous = stack.pop()
            char = s[node]
            if not exiting:
                # Find the closest ancestor with the same character
                if char in last and node != 0:
                    new_parent[node] = last[char]
                # Remember the previous ancestor with this character
                previous = last.get(char)
                # Current node becomes the latest ancestor
                last[char] = node
                # Add an exit event to restore the previous value
                stack.append((node, True, previous))
                # Visit the orignal children
                for child in reversed(children[node]):
                    stack.append((child, False, None))

            else:
                # Restore the previous ancestor when DFS exits this node
                if previous is None:
                    del last[char]
                else:
                    last[char] = previous

        # Build the modified tree
        new_children = [[] for _ in range(n)]

        for node in range(1, n):
            new_children[new_parent[node]].append(node)

        # Second DFS: Get nodes in traversal order
        order = [0]

        for node in order:
            for child in new_children[node]:
                order.append(child)

        # Initially, every node has a subtree size of 1
        answer = [1] * n

        # Process children before their parents
        for node in reversed(order):
            if node != 0:
                answer[new_parent[node]] += answer[node]

        return answer
