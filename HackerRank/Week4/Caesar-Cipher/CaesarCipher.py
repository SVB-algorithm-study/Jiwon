#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def cipherDict(start, end, k):
    cipher = defaultdict(str)
    for i in range(start, end + 1):
        caesar = i + k
        if caesar > end:
            caesar -= 26
        cipher[chr(i)] = chr(caesar)
    return cipher


def caesarCipher(s, k):
    # Write your code here
    # 26 alphabets
    k = k % 26
    # a~z: 97~122
    lower = cipherDict(97, 122, k)
    # A~Z: 65~90
    upper = cipherDict(65, 90, k)

    answer = []
    for element in s:
        if element.isupper():
            answer.append(upper[element])
        elif element.islower():
            answer.append(lower[element])
        else:
            answer.append(element)

    return "".join(answer)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + "\n")

    fptr.close()
