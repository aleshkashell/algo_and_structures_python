"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def get_sum(count, divident=1):
    if count == 0:
        return 0
    else:
        return divident + get_sum(count-1, divident/2)


if __name__ == '__main__':
    num = int(input("Введите количестов элементов последовательности: "))
    print(f'Сумма последовательности: {get_sum(num)}')
