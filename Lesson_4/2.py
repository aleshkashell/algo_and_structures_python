"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
from timeit import timeit
import math


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


if __name__ == '__main__':
    number = 10000
    n = 11
    print("Время выполнения обычной функции: ", end='')
    print(timeit(f'get_primes({n})', setup='from __main__ import get_primes', number=number))
    print("Время выполнения решета Эратосфена: ", end='')
    print(timeit(f'primes_sieve({n})', setup='from __main__ import primes_sieve', number=number))

"""
Нахождение 10-го числа (1000000 запусков):
Время выполнения обычной функции: 7.015490589001274
Время выполнения решета Эратосфена: 7.9177059270004975

Нахождение 100-го числа (1000 запусков):
Время выполнения обычной функции: 1.7657503859954886
Время выполнения решета Эратосфена: 1.1618186120031169

Нахождение 1000000-го числа:
Время выполнения обычной функции: 76.8135189780005
Время выполнения решета Эратосфена: 4.909552088000055


Сложность решета Эратосфена O(n log(n)), второго алгоритма - O(n).
Из результатов можно сделать вывод, что алгоритм сложностью O(n log(n)) гораздо эффективнее с увеличением количетва элементов,
а в данном примере преимущество решета Эратосфена проявляется начиная с 11 элементов.

"""