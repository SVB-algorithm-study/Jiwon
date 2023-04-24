#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr, n):
    # Write your code here
    left_to_right = sum([arr[m][m] for m in range(n)])
    right_to_left = sum([arr[n - 1 - i][i] for i in range(n)])
    return abs(left_to_right - right_to_left)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + "\n")

    fptr.close()
