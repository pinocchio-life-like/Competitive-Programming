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
    for grade in grades:
        if grade < 38:
            pass
        elif grade >= 100:
            pass
        elif int(repr(grade)[-1]) > 5:
            addr = 10 - int(repr(grade)[-1])
            if addr >= 3:
                pass
            else:
                index = grades.index(grade)
                grades[index] = grade+addr

        elif int(repr(grade)[-1]) < 5:
            addr = 5 - int(repr(grade)[-1])
            if addr >= 3:
                pass
            else:
                index = grades.index(grade)
                grades[index] = grade + addr
    return grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
