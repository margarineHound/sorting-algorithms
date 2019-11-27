import numpy as np
import random
import time

def quicksort(A):
    random.seed(time.time())
    length = len(A)
    l = 0
    r = length-1
    def qsort(A, l, r):
        if l >= r:
            return


        p = choosePivot(l, r)
        pivot = A[p]
        if p != l:
            swap(p, l, A)
        divider = Parition(A, l, r, pivot)
        qsort(A, l, divider-2)
        qsort(A, divider, r)

    qsort(A, l, r)
    return

def swap(i, j, A):

    temp = A[i]
    A[i]= A[j]
    A[j] = temp
    return

def Parition(A, l, r, pivot):
    i = l+1
    for j in range(i, r+1):
        if A[j] < pivot:
            swap(i, j, A)
            i += 1

    swap(l, i-1, A)
    return i

def choosePivot(l, r):
     return random.randint(l, r)

if __name__ == "__main__":

    arr = list(range(1,200))
    random.shuffle(arr)
    print(arr)
    quicksort(arr)
    isSorted = True
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            isSorted = False
            break

    print(arr)
    if isSorted == False:
        print("Not Sorted")
    else:
        print("Sorted")