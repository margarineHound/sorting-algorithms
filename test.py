from selection_sort import select_sort

def main():
   array = []
   array.extend(range(30,0, -1))
   print(array)
   result = select_sort(array)
   print(result)

if __name__ == '__main__':
    main()