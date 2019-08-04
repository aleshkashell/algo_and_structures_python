"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def is_even(digit):
    if digit % 2 == 1:
        return 0
    else:
        return 1


def get_count(number, even=0):
    if number < 10:
        return is_even(number)
    else:
        return even + is_even(number % 10) + get_count(int(number / 10), even)


if __name__ == '__main__':
    num = int(input("Введите число: "))
    even = get_count(num)
    print(f'Число {num} имеет ', end='')
    total = 0
    while num > 0:
        total = total + 1
        num = num // 10
    print(f'{even} четных и {total - even} нечетных цифр')
