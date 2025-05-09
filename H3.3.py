class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == 0):
                    row.append(i)
                    col.append(j)
        for i in row:
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
        for j in col:
            for k in range(len(matrix)):
                matrix[k][j] = 0;
