class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:
            # move the 4 pointers
            for i in range(right - left):
                top, bottom = left, right

                topLeft = matrix[top][left + i]

                # bottom left => top left
                matrix[top][left + i] = matrix[bottom - i][left]
                # bottom right => bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # top right => bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                # tmp => top right
                matrix[top + i][right] = topLeft
            left += 1
            right -= 1
