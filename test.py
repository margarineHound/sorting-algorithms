from selection_sort import select_sort
from merge_sort import merge_sort

def strictly_increasing(L):
    return all(x<y for x, y in zip(L, L[1:]))


def main():
   array = []
   array.extend(range(1000000,0, -1))
   # array = [8,7,6,5,4,3,2,1]
   # array.extend([1,12,12,12,12,12,12,12,12,13,24,24,24])
   # print(array)
   result = merge_sort(array)
   # print(result)
   value = strictly_increasing(result)
   print(repr(value))

if __name__ == '__main__':
    main()
