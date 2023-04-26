#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(string):
    # Write your code here
    alpha_dict = {chr(alpha): 1 for alpha in range(97, 123)}

    # remove spaces from string
    string = string.replace(" ", "").lower()

    # if the string length is smaller than 26, it can't be pangram
    if len(string) < 26:
        return "not pangram"
    for s in string:
        if alpha_dict[s] == 1:
            alpha_dict[s] -= 1

    return "pangram" if sum(alpha_dict.values()) == 0 else "not pangram"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = pangrams(s)

    fptr.write(result + "\n")

    fptr.close()
