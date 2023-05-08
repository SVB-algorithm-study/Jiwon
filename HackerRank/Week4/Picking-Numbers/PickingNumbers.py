#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    # Write your code here
    a.sort()
    count = list(Counter(a).items())
    res = max(count[0][1], count[-1][1])

    for i in range(len(count) - 1):
        num, cnt = count[i]
        res = max(res, cnt)
        next_num, next_cnt = count[i + 1]

        if abs(next_num - num) <= 1:
            res = max(res, cnt + next_cnt)

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + "\n")

    fptr.close()
