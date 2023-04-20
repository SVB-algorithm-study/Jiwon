class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])

        zeros = {"r": set(), "c": set()}
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zeros["r"].add(r)
                    zeros["c"].add(c)

        # all rows to zero
        for r in zeros["r"]:
            for i in range(col):
                matrix[r][i] = 0
        for c in zeros["c"]:
            for j in range(row):
                matrix[j][c] = 0
