#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)
    _sum = 0
    for i in range(n // 2):
        for j in range(n // 2):  # column
            _sum += max(
                matrix[i][j],
                matrix[i][n - j - 1],
                matrix[n - i - 1][j],
                matrix[n - i - 1][n - j - 1],
            )

    return _sum
