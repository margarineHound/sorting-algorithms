#!/usr/bin/python3

def search(lst):

    length = len(lst)
    for n in range(length):
        smallest = n
        for k in range(lst[n+1]):
