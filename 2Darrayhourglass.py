#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
a = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    a.append(arr_t)

smax = -9 * 7
s=0
for r in range(1,5):
    for c in range(1,5):
        s=a[r-1][c-1]+a[r-1][c]+a[r-1][c+1]+a[r][c]+a[r+1][c-1]+a[r+1][c]+a[r+1][c+1]
        smax = max(s, smax)

print(smax)
