from selection_sort import select_sort
from merge_sort import merge_sort

def main():
   array = []
   array.extend(range(30,0, -1))
   print(array)
   result = merge_sort(array)
   print(result)

if __name__ == '__main__':
    main()