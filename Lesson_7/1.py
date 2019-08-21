"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint


def get_array(length=20):
    return [randint(-100, 99) for i in range(length)]


def buble_sort(array):
    changed = False
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                changed = True
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
        if changed:
            changed = False
        else:
            break


def main():
    array = get_array()
    print(f'Исходный массив:\n{array}')
    buble_sort(array)
    print(f'Отсортированный массив:\n{array}')


if __name__ == '__main__':
    main()
