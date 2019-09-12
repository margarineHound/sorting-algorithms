def merge_sort(*args):
    temp1 = None
    temp2 = None
    op = None
    templist = args[0]
    l = []

    if len(templist) > 1:
        for i in templist:
            m = int(len(templist)/2)
            op = merge_sort(templist[:m], templist[m+1:])
    else:
        return [templist]
    if len(op[0])>len(op[1]):
        temp1 = 0
        temp2 = 1
    else:
        temp1 = 1
        temp2 = 0
    while op[temp1]:
        if op[temp1][0] > op[temp2][0]:
            l.append(op[temp2][0])
            del op[temp2][0]
            if not op[temp2]:
                l.extend(temp1)
                return l
            else:
                continue
        else:
            l.append(op[temp1][0])
            del op[temp1][0]
            if not op[temp1]:
                l.extend(temp2)
                return l
            else:
                continue

    return l
def main():
    pass
if __name__ == '__main__':
    main()