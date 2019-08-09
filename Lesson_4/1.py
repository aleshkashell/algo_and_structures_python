"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
from timeit import timeit
import cProfile


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


def profile():
    cProfile.run('analyze_time()')


def analyze_time(num=40):
    number = 1000000
    print("Время выполнения рекурсивной функции: ", end='')
    print(timeit(f'get_sum_recursive({num})', setup='from __main__ import get_sum_recursive', number=number))
    print("Время выполнения рекурсивной функции с мемоизацией: ", end='')
    print(timeit(f'get_sum_recursive_mem({num})', setup='from __main__ import get_sum_recursive_mem', number=number))
    print("Время выполнения цикла: ", end='')
    print(timeit(f'get_sum_loop({num})', setup='from __main__ import get_sum_loop', number=number))
    print("Время выполнения цикла с мемоизацией: ", end='')
    print(timeit(f'get_sum_loop_mem({num})', setup='from __main__ import get_sum_loop_mem', number=number))


if __name__ == '__main__':
    profile()


"""
Время выполнения рекурсивной функции: 10.685293730999547
Время выполнения рекурсивной функции с мемоизацией: 0.36603713300064555
Время выполнения цикла: 2.8995167309985845
Время выполнения цикла с мемоизацией: 0.3632724329982011
         46000144 function calls (6000101 primitive calls) in 13.856 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1000000    0.154    0.000    0.222    0.000 1.py:11(g)
  1000000    0.154    0.000    0.220    0.000 1.py:21(g)
41000040/1000001   10.511    0.000   10.511    0.000 1.py:30(get_sum_recursive)
  1000000    2.759    0.000    2.759    0.000 1.py:37(get_sum_loop)
        1    0.000    0.000    0.000    0.000 1.py:46(get_sum_loop_mem)
        1    0.000    0.000    0.000    0.000 1.py:56(get_sum_recursive_mem)
        1    0.000    0.000   14.315   14.315 1.py:68(analyze_time)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
        1    0.000    0.000   14.315   14.315 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 <timeit-src>:2(<module>)
        1    0.143    0.143    0.363    0.363 <timeit-src>:2(inner)
        4    0.000    0.000    0.001    0.000 timeit.py:100(__init__)
        4    0.000    0.000   14.314    3.579 timeit.py:162(timeit)
        4    0.000    0.000   14.315    3.579 timeit.py:229(timeit)
        8    0.000    0.000    0.000    0.000 timeit.py:78(reindent)
       12    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
      5/1    0.000    0.000   14.315   14.315 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.globals}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        4    0.000    0.000    0.000    0.000 {built-in method gc.disable}
        4    0.000    0.000    0.000    0.000 {built-in method gc.enable}
        4    0.000    0.000    0.000    0.000 {built-in method gc.isenabled}
        8    0.000    0.000    0.000    0.000 {built-in method time.perf_counter}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
  2000000    0.133    0.000    0.133    0.000 {method 'get' of 'dict' objects}
        8    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}

#################################################################################################

Сложностью как "циклического", так и рекусрсивного алгоритма является O(n), т.к. количество итераций напрямую зависит
от количества элементов и растет линейно.

#################################################################################################

Из полученных резульатов можем утверждать, что самым не эффективным алгоритмом является рекурсия.
Цикл является более преемлемым способом, и самыми предпочтительными вариантами я являются те же алгоритмы, но с 
использованием мемоизации, а в случае длительных расчетов лучше обойтись "циклическими" алгоритмами, т.к. 
на рекурсивных алгоритмов происходит огромное количество запусков функций, на что тратятся ресурсы и время. 
Это хорошо видно в данном примере, т.к. при одинаковой сложности и входных данных рекурсивный алгоритм 
занимает в >3 раза больше времени на выполнение.

#################################################################################################

Т.о., на мой взгляд, правильным будет использовать рекурсивные алгоритмы только там, где они будут более наглядными в коде,
либо значительно упрощать логику кода и очень обдуманно подходить к ним при использовании длинных последовательностей.

"""