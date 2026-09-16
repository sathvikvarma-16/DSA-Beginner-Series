class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min = []
        col_max = []
        for row in matrix:
            row_min.append(min(row))
        for j in range(len(matrix[0])):
            maximum = matrix[0][j]
            for i in range(len(matrix)):
                if matrix[i][j] > maximum:
                    maximum = matrix[i][j]
            col_max.append(maximum)
        ans = []
        for num in row_min:
            if num in col_max:
                ans.append(num)
        return ans