"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
from random import randint


def get_array(length=20):
    return [randint(-100, 99) for i in range(2 * length + 1)]


def heapify(array, length, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < length and array[i] < array[l]:
        largest = l
    if r < length and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, length, largest)


def heap_sort(array):
    length = len(array)

    for i in range(length, -1, -1):
        heapify(array, length, i)
    for i in range(length-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)



def main():
    array = get_array()
    middle = len(array) // 2
    print(f'Исходный массив:\n{array}')
    heap_sort(array)
    print(f'Медиана: {array[middle]}')
    print(f'Элементы не больше медианы:\n{array[:middle]}')
    print(f'Элементы не меньше медианы:\n{array[middle+1:]}')


if __name__ == '__main__':
    main()