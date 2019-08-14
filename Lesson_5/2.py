"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque
from itertools import zip_longest


class HexNum:
    def __init__(self, text=''):
        self.data = deque([i for i in text])

    def __add__(self, other):
        result = HexNum()
        addit = 0
        for a, b in zip_longest(reversed(self.data), reversed(other.data), fillvalue='0'):
            digit_sum = int(a, 16) + int(b, 16) + addit
            result.appendleft(f"{digit_sum % 16:X}")
            addit = digit_sum // 16
        if addit > 0:
            result.appendleft(f"{addit % 16:X}")
        return result

    def appendleft(self, text_digit):
        self.data.appendleft(text_digit)

    def __mul__(self, other):
        result = HexNum()
        addit = 0
        for i, a in enumerate(reversed(self.data)):
            tmp_result = HexNum('0' * i)
            for b in reversed(other.data):
                digit_mul = int(a, 16) * int(b, 16) + addit
                tmp_result.appendleft(f"{digit_mul % 16:X}")
                addit = digit_mul // 16
            result = result + tmp_result
            while addit > 0:
                result.appendleft(f"{addit % 16:X}")
                addit = addit // 16
        return result

    def __str__(self):
        delim = "', '"
        return f"['{delim.join(self.data)}']"

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    numbers = [HexNum(i) for i in input("Введите шестнадцатиричные числа, разделяя пробелами: ").split()]
    summ = HexNum()
    mult = HexNum('1')
    for i in numbers:
        summ = summ + i
        mult = mult * i
    print(f"Вы ввели следующие числа: {', '.join([str(i) for i in numbers])}")
    print(f"Их сумма: {summ}")
    print(f"Из произведение: {mult}")
