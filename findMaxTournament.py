'''
find max value and return the lost of comparisons made prior
'''


def findMaxTournament(length, arr):
    if length == 1:
        Compared = [1, arr[0]]
        return Compared

    midpoint = int(length/2)
    Compared1 = findMaxTournament(len(arr[0:midpoint]), arr[0: midpoint])
    Compared2 = findMaxTournament(len(arr[midpoint:]), arr[midpoint:])

    if Compared1[1] > Compared2[1]:
        Compared1[0] +=  1
        Compared1.append(Compared2[1])
        return Compared1


    else:
        Compared2[0] += 1
        Compared2.append(Compared1[1])
        return Compared2

def main():
    pass

if __name__ == "__main__":
    main()