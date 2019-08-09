"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
from timeit import timeit


def memorize(func):
    def g(n, divident=1, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n, divident)
            memory[n] = r
        return r
    return g


def memorize_loop(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


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


@memorize_loop
def get_sum_loop_mem(count):
    divident = 1
    sum = 1
    for i in range(1, count):
        divident = divident / -2
        sum = sum + divident
    return sum


@memorize
def get_sum_recursive_mem(count, divident=1):
    if count == 0:
        return 0
    else:
        return divident + get_sum_recursive(count-1, divident/-2)


def analyze_time(num):
    print("Время выполнения рекурсивной функции: ", end='')
    print(timeit('get_sum_recursive(num)', setup='from __main__ import get_sum_recursive, num'))
    print("Время выполнения рекурсивной функции с мемоизацией: ", end='')
    print(timeit('get_sum_recursive_mem(num)', setup='from __main__ import get_sum_recursive_mem, num'))
    print("Время выполнения цикла: ", end='')
    print(timeit('get_sum_loop(num)', setup='from __main__ import get_sum_loop, num'))
    print("Время выполнения цикла с мемоизацией: ", end='')
    print(timeit('get_sum_loop_mem(num)', setup='from __main__ import get_sum_loop_mem, num'))


if __name__ == '__main__':
    num = 40
    analyze_time(40)
