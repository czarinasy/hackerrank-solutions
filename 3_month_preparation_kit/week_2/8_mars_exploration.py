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
    errors = 0
    og = 'SOSSOS'
    pointer = 0

    for letter in s:
        if letter != og[pointer]:
            errors += 1

        if pointer == 5:
            pointer = 0
        else:
            pointer += 1

    return errors


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
