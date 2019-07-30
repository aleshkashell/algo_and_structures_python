"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
from random import random


if __name__ == '__main__':
    start = input('Введите начало диапазона: ')
    end = input('Введите конец диапазона: ')

    if start.isdigit() and end.isdigit():
        print(int(random() * (int(end) - int(start) + 1) + int(start)))
    elif start.isalpha() and end.isalpha():
        print(chr(int(random() * (ord(end) - ord(start) + 1) + ord(start))))
    else:
        try:
            m1 = float(start)
            m2 = float(end)
            print(round(random() * (m2 - m1) + m1, 3))
        except ValueError:
            print("Wrong numbers")