#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def marsExploration(s):
    # Write your code here
    origin_signal = "SOS"
    cnt = 0
    for i in range(0, len(s), 3):
        received_signal = s[i : i + 3]
        for s1, s2 in zip(origin_signal, received_signal):
            if s1 != s2:
                cnt += 1

    return cnt


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + "\n")

    fptr.close()
