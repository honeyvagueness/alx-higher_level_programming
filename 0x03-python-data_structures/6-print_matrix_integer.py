#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        fmt = " ".join(["{:d}" for x in row])
        print(fmt.format(*row))


if __name__ == '__main__':
    mat = [[a, a+1, a+2] for a in range(1, 16, 3)]
    print_matrix_integer(mat)
