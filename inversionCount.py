
invs = 0

def readFile(f):
    array = []
    for i in f:
        array.append(int(i))

    return array

def mergeSort(intArr):
    if len(intArr) < 2:
        return intArr

    length = len(intArr)
    arr1 = mergeSort(intArr[:int(length/2)])
    arr2 = mergeSort(intArr[int(length/2):])

    return mergeCombine(arr1, arr2)

def mergeCombine(intArr1, intArr2):
    global invs
    arrTotal = []
    if type(intArr1) != list:
        intArr1 = [intArr1]
    if type(intArr2) != list:
        intArr2 = [intArr2]
    while len(intArr1) > 0:
        if intArr1[0] < intArr2[0]:

            arrTotal.append(intArr1[0])
            del intArr1[0]
        else:

            arrTotal.append(intArr2[0])
            del intArr2[0]
            invs += len(intArr1)
        if len(intArr1)<1:
            arrTotal.extend(intArr2)
            return arrTotal
        elif len(intArr2) < 1:
            arrTotal.extend(intArr1)
            return arrTotal


    return invs
def main():
    global invs
    try:
        f = open("IntegerArray.txt")
        intArr = readFile(f)
    finally:
        f.close()


    sortedArr = mergeSort(intArr)
    print(invs)

if __name__ == "__main__":
    main()
