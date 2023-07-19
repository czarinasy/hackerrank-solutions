#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here

    cur_level = 0

    prev_level = -1

    valley_counter = 0

    for step in path:
        prev_level = cur_level

        if step == 'D':
            cur_level -= 1
        elif step == 'U':
            cur_level += 1

        if (prev_level == 0) and (cur_level == -1):
            valley_counter += 1

    return valley_counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
