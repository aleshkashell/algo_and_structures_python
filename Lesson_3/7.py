"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from random import randint


def generate_array(count=20):
    random_array = [0] * count
    for i in range(0, len(random_array)):
        random_array[i] = randint(-50, 50)
    return random_array


def find_min_elements(array):
    first = array[0]
    second = array[1]
    for i in range(2, len(array)):
        if first < second:
            if array[i] < second:
                second = array[i]
        elif second < first:
            if array[i] < first:
                first = array[i]
        else:
            if array[i] < first:
                first = array[i]
    return first, second

if __name__ == '__main__':
    random_array = generate_array()
    print(f'Исходный массив:\n{random_array}')
    print(f'Минимальные элементы: {find_min_elements(random_array)}')