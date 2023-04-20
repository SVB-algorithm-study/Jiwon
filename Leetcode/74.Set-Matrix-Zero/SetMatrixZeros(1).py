class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])

        # find zero position
        zeros = []
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zeros.append((r, c))

        # replace all rows and columns to zero
        for r, c in zeros:
            # all rows to zero
            for i in range(row):
                matrix[i][c] = 0
            # all columns to zero
            for j in range(col):
                matrix[r][j] = 0
