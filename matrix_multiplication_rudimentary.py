import math

def mmultiply(x, y):
    x_row = len(x)
    x_col = len(x[0])

    y_row = len(x)
    y_col = len(x[0])

    result = [[0 for k in range(y_col)] for i in range(x_row)]


    if x_col != y_row:
        raise Exception

    for i in range(x_row):
        row = x[i]
        for j in range(y_col):
            col = [y[l][j] for l in range(y_row)]
            for l in range(len(col)):
                result[i][j] += row[l]*col[l]


    return result

def main():
    mat1 = [[0 for j in range(5)] for i in range(5)]
    mat1[0][0], mat1[1][1], mat1[2][2], mat1[3][3], mat1[3][3] = 1, 1, 1, 1, 1
    matrix = [[3, 1, 2, 3, 4], [0, 0, 4, 0, 0], [0, 0, 5, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
    result = mmultiply(matrix, mat1)
    print(result)

if __name__ == '__main__':
    main()
