"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from memory_profiler import profile
from pympler.asizeof import asizeof
import math


@profile
def get_primes(index):
    primes = [2]
    i = 1
    while True:
        if len(primes) >= index:
            break
        i = i + 2
        if (i > 10) and (i%10 == 5):
            continue
        for j in primes:
            if j * j - 1 > i:
                primes.append(i)
                break
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes[len(primes)-1]


@profile
def primes_sieve(index):
    if index == 1:
        return 2
    if index < 7:
        coef = 3
    else:
        coef = 1.4
    limit = int(index * math.log(index) * coef)
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    primes = list()

    for (i, isprime) in enumerate(a):
        if isprime:
            primes.append(i)
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
    # print(primes)
    return primes[index-1]


@profile
def main():
    n = 50000
    print(primes_sieve(n))
    print(get_primes(n))


if __name__ == '__main__':
    main()


"""
Filename: /home/a.sheludchenkov/geekbrains/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    35     34.3 MiB     34.3 MiB   @profile
    36                             def primes_sieve(index):
    37     34.3 MiB      0.0 MiB       if index == 1:
    38                                     return 2
    39     34.3 MiB      0.0 MiB       if index < 7:
    40                                     coef = 3
    41                                 else:
    42     34.3 MiB      0.0 MiB           coef = 1.4
    43     34.3 MiB      0.0 MiB       limit = int(index * math.log(index) * coef)
    44     40.2 MiB      5.9 MiB       a = [True] * limit                          # Initialize the primality list
    45     40.2 MiB      0.0 MiB       a[0] = a[1] = False
    46     40.2 MiB      0.0 MiB       primes = list()
    47                             
    48     42.4 MiB      0.3 MiB       for (i, isprime) in enumerate(a):
    49     42.4 MiB      0.0 MiB           if isprime:
    50     42.4 MiB      0.3 MiB               primes.append(i)
    51     42.4 MiB      0.0 MiB               for n in range(i*i, limit, i):     # Mark factors non-prime
    52     40.2 MiB      0.0 MiB                   a[n] = False
    53                                 # print(primes)
    54     42.4 MiB      0.0 MiB       return primes[index-1]


611953
Filename: /home/a.sheludchenkov/geekbrains/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    14     35.1 MiB     35.1 MiB   @profile
    15                             def get_primes(index):
    16     35.1 MiB      0.0 MiB       primes = [2]
    17     35.1 MiB      0.0 MiB       i = 1
    18     35.1 MiB      0.0 MiB       while True:
    19     36.4 MiB      0.0 MiB           if len(primes) >= index:
    20     36.4 MiB      0.0 MiB               break
    21     36.4 MiB      0.2 MiB           i = i + 2
    22     36.4 MiB      0.0 MiB           if (i > 10) and (i%10 == 5):
    23     36.4 MiB      0.0 MiB               continue
    24     36.4 MiB      0.0 MiB           for j in primes:
    25     36.4 MiB      0.0 MiB               if j * j - 1 > i:
    26     36.4 MiB      0.0 MiB                   primes.append(i)
    27     36.4 MiB      0.0 MiB                   break
    28     36.4 MiB      0.0 MiB               if i % j == 0:
    29     36.4 MiB      0.0 MiB                   break
    30                                     else:
    31     35.1 MiB      0.0 MiB               primes.append(i)
    32     36.4 MiB      0.0 MiB       return primes[len(primes)-1]


611953
Filename: /home/a.sheludchenkov/geekbrains/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    57     34.3 MiB     34.3 MiB   @profile
    58                             def main():
    59     34.3 MiB      0.0 MiB       n = 50000
    60     35.1 MiB      0.9 MiB       print(primes_sieve(n))
    61     35.4 MiB      0.3 MiB       print(get_primes(n))






Из результатов видно, что алгоритм рещето Эратосфена имеет большее потребление памяти, т.к. для вычисления он хранит в памяти
информацию обо всех числах, меньших искомого простого.
Наивный алгоритм хранит только простые числа в плоть до искомого, что позволяет ему потребять значительно меньше памяти.
Он достаточно оптимизирован в плане потребления памяти.

Решето Эратосфена возможно оптимизировать по памяти, если создать дополнительный массив для простых чисел и производить
вычисления кусками. Т.е. в первую итерацию просеять миллион значений, заполнить массив с простыми числами. На следующих 
итерациях снова использовать миллион значений и просеивать его на основе массива с простыми числами. 
"""