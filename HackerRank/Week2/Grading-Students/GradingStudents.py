#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    # Write your code here
    new_grades = []
    for grade in grades:
        # if the grade is less than 38
        if grade < 38:
            new_grades.append(grade)
            continue
        # else check the difference with next multiple of 5
        next_mul = 5 * ((grade // 5) + 1)
        if next_mul - grade < 3:
            new_grades.append(next_mul)
        else:
            new_grades.append(grade)

    return new_grades


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
