# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint


def generate_array(count=20):
    random_array = [0] * count
    for i in range(0, len(random_array)):
        random_array[i] = randint(-50, 50)
    return random_array


def generate_matrix(row, column):
    return [generate_array(column) for _ in range(row)]


def get_min_element(arr):
    element = 0
    for i in range(0, len(arr)):
        if arr[i] < element:
            element = arr[i]
    return element


def print_matrix(matrix):
    for i in matrix:
        print('|', end='')
        for j in i:
            print(f'{j:5}', end='')
        print(' |')


if __name__ == '__main__':
    row = 4
    column = 4
    matrix = generate_matrix(row, column)
    print_matrix(matrix)
    min_elements = list()
    for i in range(column):
        column = list()
        for j in range(row):
            column.append(matrix[j][i])
        min_elements.append(get_min_element(column))
    sum = 0
    print(f'Минимальные элементы: {min_elements}')
    for i in min_elements:
        sum = sum + i
    print(f'Сумма минимальных елементов: {sum}')
