"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""


def get_sum_recursive(count, divident=1):
    if count == 0:
        return 0
    else:
        return divident + get_sum_recursive(count-1, divident/-2)


def get_sum_loop(count):
    divident = 1
    sum = 1
    for i in range(1, count):
        divident = divident / -2
        sum = sum + divident
    return sum


if __name__ == '__main__':
    num = 40
    print(get_sum_recursive(num))
    print(get_sum_loop(num))
