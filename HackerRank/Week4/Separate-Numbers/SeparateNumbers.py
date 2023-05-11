#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#


def separateNumbers(s):
    # Write your code here
    l = 1
    while l <= len(s) // 2:
        sequence = [int(s[:l])]

        while len("".join(sequence)) < len(s):
            sequence.append(sequence[-1] + 1)

        if "".join(list(sequence)) == s:
            print("YES")
            return
        l += 1
    print("NO")


if __name__ == "__main__":
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
