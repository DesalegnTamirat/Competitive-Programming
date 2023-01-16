#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    tobesorted = arr[n-1]
    for i in range(n):
        c = 0
        if tobesorted < arr[n - 2 - i] and i != n - 1:
            arr[n - 1 - i] = arr[n - 2 - i]
        else:
            arr[n - 1 - i] = tobesorted
            c = 4
        ar = list(map(str, arr))
        print(' '.join(ar))
        if c == 4:
            break
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
