def lenCheck(matrix):
    if len(matrix) > 1:
        pass
    while((len(mat1)> 1 or len(mat1[0])> 1 ) and (len(mat1)%2 != 0 or len(mat1[0])%2 != 0)):
        pass
    while((len(mat2)> 1 or len(mat2[0])> 1 ) and (len(mat2)%2 != 0 or len(mat2[0])%2 != 0)):
        pass
    if len(mat1)> 1 and len(mat1)%2 != 0:
        for i in range(len(mat1)):
            mat1[i].append(0)

        temp = [[0 for x in len(range(mat1))]]
        mat1.extend(temp)

    if len(mat2)> 1 and len(mat2)%2 != 0:
        for i in range(len(mat2)):
            mat1[i].append(0)

        temp = [[0 for x in len(range(mat2))]]
        mat2.extend(temp)

def mat_resize(matrix):
    pass

def mat_add(matrix):
    pass

def mat_sub(matrix):
    pass

def strassen(mat1, mat2):
    '''
    #   This is an algorithm that works only on nxn matrices,
    #   where both matrix 1 and matrix 2 are of equal dimensions
    # '''

    if len(mat1) == 1 and len(mat2) == 2:
        return mat1[0] * mat2[0]

    # matA = strassen(int(mat1))