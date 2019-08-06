"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint


def generate_array(count=20):
    random_array = [0] * count
    for i in range(0, len(random_array)):
        random_array[i] = randint(-50, 50)
    return random_array


def get_max_index(arr):
    index = 0
    for i in range(0, len(arr)):
        if arr[i] > arr[index]:
            index = i
    return index


def get_min_index(arr):
    index = 0
    for i in range(0, len(arr)):
        if arr[i] < arr[index]:
            index = i
    return index


def get_sum(arr, start, end):
    sum = 0
    if start > end:
        for i in range(end + 1, start):
            sum = sum + arr[i]
    else:
        for i in range(start + 1, end):
            sum = sum + arr[i]
    return sum


if __name__ == '__main__':
    random_array = generate_array()
    print(f'Исходный массив:\n{random_array}')

    max = get_max_index(random_array)
    min = get_min_index(random_array)
    print(f'Минимальный элемент {random_array[min]}, индекс: {min}')
    print(f'Максимальный элемент {random_array[max]}, индекс: {max}')
    sum = get_sum(random_array, min, max)
    print(f'Сумма элементов между максимальным и минимальным {sum}')
