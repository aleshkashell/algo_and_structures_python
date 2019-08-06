"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
from random import randint


def generate_array(count=20):
    random_array = [0] * count
    for i in range(0, len(random_array)):
        random_array[i] = randint(-50, 50)
    return random_array


if __name__ == '__main__':
    # input matrix
    matrix = [generate_array(4) for _ in range(4)]
    # count matrix
    matrix.append([0] * 4)
    for i in range(0, 4):
        for j in range(0, 4):
            matrix[4][i] = matrix[4][i] + matrix[j][i]
    for i in matrix:
        print('|', end='')
        for j in i:
            print(f'{j:5}', end='')
        print(' |')