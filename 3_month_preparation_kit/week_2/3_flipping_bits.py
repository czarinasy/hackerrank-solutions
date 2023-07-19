#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    n_bits = f'{n:032b}'
    print(n_bits)

    flipped_bits = ''

    for bit in n_bits:
        if bit == '1':
            flipped_bits += '0'
        elif bit == '0':
            flipped_bits += '1'

    return int(flipped_bits, 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
