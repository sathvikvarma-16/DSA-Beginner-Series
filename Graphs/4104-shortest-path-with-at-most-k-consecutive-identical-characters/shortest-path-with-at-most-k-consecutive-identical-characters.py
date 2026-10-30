class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        import heapq
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        # dist[node][count]
        # Minimum cost to reach node with count
        # consecutive occurrences of labels[node]
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]
        # Starting node
        dist[0][1] = 0
        # (cost, node, count)
        pq = [(0, 0, 1)]
        while pq:
            cost, node, count = heapq.heappop(pq)
            # Skip outdated states
            if cost != dist[node][count]:
                continue
            # Destination reached
            if node == n - 1:
                return cost
            # Explore neighbours
            for neighbor, weight in graph[node]:
                # Same consecutive character
                if labels[neighbor] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1
                # Reject invalid paths
                if new_count > k:
                    continue
                new_cost = cost + weight
                # Relaxation
                if new_cost < dist[neighbor][new_count]:
                    dist[neighbor][new_count] = new_cost
                    heapq.heappush(
                        pq,
                        (new_cost, neighbor, new_count)
                    )
        return -1