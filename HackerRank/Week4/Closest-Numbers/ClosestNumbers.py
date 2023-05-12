#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def closestNumbers(arr):
    # Write your code here
    arr.sort()

    differ_dict = defaultdict(list)

    for i in range(len(arr) - 1):
        differ = arr[i + 1] - arr[i]
        differ_dict[differ].append((arr[i], arr[i + 1]))

    min_differs = differ_dict[min(differ_dict.keys())]

    return [item for tup in min_differs for item in tup]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
