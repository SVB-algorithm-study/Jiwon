#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#


def swap(l, r, arr):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1
    return arr


def rotateLeft(d, arr):
    # Write your code here
    l, r = 0, len(arr) - 1
    arr = swap(l, r, arr)
    print(arr)

    l, r = 0, len(arr) - d - 1
    arr = swap(l, r, arr)

    l, r = len(arr) - d, len(arr) - 1
    arr = swap(l, r, arr)

    return arr


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
