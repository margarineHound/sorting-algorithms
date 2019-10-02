def merge_sort(*args):
    '''
    takes in an array, and returns a sorted array, and the number of inversions
    returns a tuple count, array
    '''
    # temp1 = None
    # temp2 = None
    # op = None
    templist = args[0]
    l = []

    if len(templist) > 1:
        m = int(len(templist)/2)
        [op1, count1] = merge_sort(templist[:m])
        [op2, count2] = merge_sort(templist[m:])
    else:
        return templist, 0
    lentot = len(op1) + len(op2)
    count = count1 + count2
    for i in range(lentot):
        if op1[0] > op2[0]:
            l.append(op2[0])
            del op2[0]
            count += len(op1)
            if not op2:
                l.extend(op1)
                return l, count
            else:
                continue
        else:
            l.append(op1[0])
            del op1[0]
            if not op1:
                l.extend(op2)
                return l, count
            else:
                continue

    return l, count
def main():
    pass
if __name__ == '__main__':
    main()