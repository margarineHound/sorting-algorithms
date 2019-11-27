from findMaxTournament import findMaxTournament


def findSecondMax(length, arr):
    Compared1 = findMaxTournament(length, arr)
    Compared2 = findMaxTournament(Compared1[0]-1, Compared1[2:])

    return Compared2[1]

def main():
    lis = [1,2,3,4,5,6,7,8,9]
    risk = findSecondMax(len(lis), lis)
    print(risk)
if __name__ == "__main__":
    main()