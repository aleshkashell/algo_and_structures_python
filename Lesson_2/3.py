"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def reverse_print(number):
    if number < 10:
        print(number, end='')
    else:
        print(number % 10, end='')
        reverse_print(number // 10)


if __name__ == '__main__':
    num = int(input("Введите число: "))
    reverse_print(num)
