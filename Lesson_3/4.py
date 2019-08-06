# 4.	Определить, какое число в массиве встречается чаще всего.
from random import randint


def generate_array(count=20):
    random_array = [0] * count
    for i in range(0, len(random_array)):
        random_array[i] = randint(-10, 10)
    return random_array


if __name__ == '__main__':
    array = generate_array()
    print(f'Исходный массив:\n{array}')
    counts = dict()
    for i in array:
        counts[i] = counts.get(i, 0) + 1
    element = 0
    element_count = 0
    for key, value in counts.items():
        if element_count < value:
            element_count = value
            element = key
    print(f'Самый частый элемент {element} встречается {element_count} раз')
