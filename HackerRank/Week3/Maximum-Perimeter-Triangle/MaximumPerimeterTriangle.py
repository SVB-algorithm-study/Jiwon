#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#


def maximumPerimeterTriangle(sticks):
    # Write your code here

    combis = list(map(list, combinations(sticks, 3)))

    _max = [-1]
    for combi in list(combis):
        combi.sort()
        a, b, c = combi[0], combi[1], combi[2]
        if a < b + c and b < a + c and c < a + b:
            cur_perimeter = a + b + c

            if cur_perimeter > sum(_max):
                _max = [a, b, c]

    return _max


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
