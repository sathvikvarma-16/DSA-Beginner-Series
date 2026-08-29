class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # rotate a matrix by 90 => transpose + reverse every row
        n = len(matrix)
        # 1. Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 2. Reverse every row
        for row in matrix:
            row.reverse()
            