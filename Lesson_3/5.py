# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
from random import randint


def generate_array(count=20):
    random_array = [0] * count
    for i in range(0, len(random_array)):
        random_array[i] = randint(-20, 10)
    return random_array


def get_max_index(arr):
    index = None
    for i in range(0, len(arr)):
        if arr[i] < 0:
            if index is None:
                index = i
            elif arr[i] > arr[index]:
                index = i
    return index


if __name__ == '__main__':
    array = generate_array()
    print(f'Исходный массив:\n{array}')
    index = get_max_index(array)

    if index is None:
        print("В массиве нет отрицательных чисел")
    else:
        print(f'Наибоьшее отрицательное число "{array[index]}" находится по индексу: {index}')
