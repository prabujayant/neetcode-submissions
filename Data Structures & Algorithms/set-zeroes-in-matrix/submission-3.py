class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row = any(matrix[0][j] == 0 for j in range(cols))
        first_col = any(matrix[i][0] == 0 for i in range(rows))

        # mark zeroes in first row/col
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # set cells to zero using markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # zero first row if needed
        if first_row:
            for j in range(cols):
                matrix[0][j] = 0

        # zero first column if needed
        if first_col:
            for i in range(rows):
                matrix[i][0] = 0
