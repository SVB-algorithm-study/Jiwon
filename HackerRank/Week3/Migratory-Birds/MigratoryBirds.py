#!/bin/python3

import math
import os
import random
import re
import sys

# from collections import Counter
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    # Write your code here
    birds_freq = Counter(arr)
    most_sighted = sorted(birds_freq.items(), key=lambda x: (-x[1], x[0]))

    return most_sighted[0][0]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
