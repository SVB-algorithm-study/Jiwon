#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def maxMin(k, arr):
    # Write your code here
    arr.sort()

    start = 0
    end = start + k - 1
    min_unfairness = float("inf")

    length = len(arr)
    while start <= length - k:
        min_unfairness = min(min_unfairness, arr[end] - arr[start])
        start += 1
        end += 1

    return min_unfairness


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + "\n")

    fptr.close()
