class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if rows * cols != r * c:
            return mat
        ans = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(0)
            ans.append(row)
        k = 0
        for i in range(rows):
            for j in range(cols):
                ans[k // c][k % c] = mat[i][j]  # k//c tells row number and k%c tells column number
                k += 1
        return ans

