#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def balancedSums(arr):
    # Write your code here
    left_sum = 0
    right_sum = sum(arr)
    criter = 0

    while criter < len(arr):
        right_sum -= arr[criter]
        print(arr[criter], left_sum, right_sum)
        if left_sum == right_sum:
            return "YES"
        left_sum += arr[criter]
        criter += 1

    return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + "\n")

    fptr.close()
