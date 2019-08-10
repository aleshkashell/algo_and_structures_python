"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import cProfile
from timeit import timeit
import math


def get_primes(count):
    primes = [2]
    i = 1
    while True:
        if len(primes) >= count:
            break
        i = i + 2
        if (i > 10) and (i%10 == 5):
            continue
        for j in primes:
            if j * j - 1 > i:
                primes.append(i)
                break
            if (i % j == 0):
                break
        else:
            primes.append(i)
    return primes


def primes_sieve(limit):
    a = [True] * int(limit)                          # Initialize the primality list
    a[0] = a[1] = False
    primes = list()

    for (i, isprime) in enumerate(a):
        if isprime:
            primes.append(i)
            for n in range(i*i, int(limit), i):     # Mark factors non-prime
                a[n] = False
    return primes


if __name__ == '__main__':
    n = 500
    border = n * math.log(n) * 1.4
    print(get_primes(n))
    print(primes_sieve(border))