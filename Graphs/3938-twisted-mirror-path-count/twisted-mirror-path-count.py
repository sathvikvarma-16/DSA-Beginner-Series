class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        # Paths entering a cell from the left (moving right)
        right = [[0] * n for _ in range(m)]
        # Paths entering a cell from above (moving down)
        down = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # Starting position
                if i == 0 and j == 0:
                    ways = 1
                elif grid[i][j] == 0:
                    ways = (right[i][j] + down[i][j]) % MOD
                else:
                    # Mirror: reflect incoming paths separately
                    if right[i][j] > 0 and i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + right[i][j]
                        ) % MOD
                    if down[i][j] > 0 and j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + down[i][j]
                        ) % MOD
                    continue
                # Empty cell: move right
                if j + 1 < n:
                    right[i][j + 1] = (
                        right[i][j + 1] + ways
                    ) % MOD
                # Empty cell: move down
                if i + 1 < m:
                    down[i + 1][j] = (
                        down[i + 1][j] + ways
                    ) % MOD
        return (right[m - 1][n - 1] +
                down[m - 1][n - 1]) % MOD