#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    arr.sort()
    if len(arr) == len(set(arr)):
        return arr[0]
    i = 0
    bird_id = 0
    freq = 0
    while i in range(len(arr)):
        count = arr.count(arr[i])
        if count > freq:
            bird_id = arr[i]
            freq = count
        i += count
    return bird_id


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
