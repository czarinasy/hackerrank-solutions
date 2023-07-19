#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort(reverse=True)
    i = 0
    while i in range(len(sticks) - 2):
        a, b, c = sticks[i], sticks[i + 1], sticks[i + 2]
        if not is_degenerate(a, b, c):
            per = [a, b, c]
            per.sort()
            return per
        i += 1
    return [-1]


def is_degenerate(a: int, b: int, c: int) -> bool:
    if (a + b > c) and (b + c > a) and (c + a > b):
        return False
    return True


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
