"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
from random import randint


def get_array(length=20):
    return [randint(0, 49) for i in range(length)]


def merge_sort(array):
    length = len(array)
    if length > 1:
        mid = length // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array



def main():
    array = get_array()
    print(f'Исходный массив:\n{array}')
    merge_sort(array)
    print(f'Отсортированный массив:\n{array}')


if __name__ == '__main__':
    main()