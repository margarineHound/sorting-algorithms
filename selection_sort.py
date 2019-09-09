#!/usr/bin/python3

def search(lst):

    length = len(lst)
    for n, idx in enumerate(lst):
        smallest = idx
        small_idx = n 
        #print(n)
        for k, idx2 in enumerate(lst[n+1:]):
            if idx2 < idx:
                smallest = idx2
                small_idx = k+n+1
        del lst[small_idx]
        lst.insert(0,smallest)
        return lst


def main():
   array = []
   array.extend(range(30,1, -1))
   print(array)
   result = search(array)
   print(result)

if __name__ == '__main__':
    main()
