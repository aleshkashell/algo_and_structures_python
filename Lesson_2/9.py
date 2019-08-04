"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def get_digit_sum(number):
    if number < 10:
        return number
    else:
        return number % 10 + get_digit_sum(number // 10)


if __name__ == '__main__':
    numbers = input("Введите числа, разделяя пробелом: ")
    max_number = ''
    max_sum = 0
    for i in numbers.split():
        cur_sum = get_digit_sum(int(i))
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_number = i
    print(f'{max_number} имеет самую большую сумму цифр: {max_sum}')