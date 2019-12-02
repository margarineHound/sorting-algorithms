def listman(A):
    A.append(999)
    def listman2(A):
        for i in range(len(A)):
            A[i] *= 2

    listman2(A)
if __name__ == "__main__":
    A = [1,2,3,4]
    listman(A)
    print(A)