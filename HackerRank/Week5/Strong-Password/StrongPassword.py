#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    special_characters = set("!@#$%^&*()-+")

    criteria = ["digit", "lower", "upper", "special"]
    strong_password = {key: False for key in criteria}

    for e in password:
        if e.isdigit():
            strong_password["digit"] = True
        if e.islower():
            strong_password["lower"] = True
        if e.isupper():
            strong_password["upper"] = True
        if e in special_characters:
            strong_password["special"] = True

    need = len([k for k, v in strong_password.items() if not v])
    len_sub = 6 - (len(password) + need)

    return need + len_sub if len_sub > 0 else need


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + "\n")

    fptr.close()
