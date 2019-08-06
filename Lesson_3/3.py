#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
from random import randint


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


if __name__ == '__main__':
    random_array = [0] * 20
    for i in range(0, len(random_array)):
        random_array[i] = randint(-50, 50)
    print(f'Исходный массив:\n{random_array}')
    max = get_max_index(random_array)
    min = get_min_index(random_array)
    tmp = random_array[max]
    random_array[max] = random_array[min]
    random_array[min] = tmp
    print(f'Результат:\n{random_array}')
