#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
# def minimumBribes(q):
#     # pass
#     bribes = 0
#     for i in reversed(range(len(q))):
#         if (q[i] > i+1):
#             if (q[i] > i+3):
#                 print("Too chaotic")
#                 return
#             else:
#                 for
#                 bribes += q[i] - (i+1)
#         else:
#             continue
#     print(bribes)
#     return

def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        if q[i] > i+3:
            print("Too chaotic")
            return
        else:
            continue

    for i in range(len(q)):
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)

if __name__ == '__main__':
    textfile = open("text.txt")
    t = int(textfile.readline())
    # textfile.read()
    # t = int(input())

    # print(t)
    for t_itr in range(t):

        n = int(textfile.readline())
        # print(n)

        q = list(map(int, textfile.readline().rstrip().split()))

        minimumBribes(q)
