"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import cProfile
from timeit import timeit


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



if __name__ == '__main__':
    print(get_primes(100))