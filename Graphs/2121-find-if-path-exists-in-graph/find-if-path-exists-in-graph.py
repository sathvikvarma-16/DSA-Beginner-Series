class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]  # Create a neighbor list for every node
        for u, v in edges:              # Read each connection
            graph[u].append(v)          # Connect u to v
            graph[v].append(u)          # Connect v to u (undirected graph)
        visited = set()                 # Store nodes already visited
        def dfs(node):
            if node == destination:     # Destination reached
                return True
            visited.add(node)           # Mark this node as visited
            for neighbor in graph[node]: # Visit all connected neighbors
                if neighbor not in visited:
                    if dfs(neighbor):   # Search from the neighbor
                        return True
            return False                # No path found from this node
        return dfs(source)              # Start searching from source
