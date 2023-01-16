#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    newarr = [0] * 100
    for i in range(n):
        newarr[arr[i]] += 1
    newarr = map(str, newarr)
    return ' '.join(list(newarr))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(''.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
