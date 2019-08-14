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
    def __init__(self, text):
        self.data = deque([i for i in text])

    def __add__(self, other):
        result = deque()
        addit = 0
        for a, b in zip_longest(reversed(self.data), reversed(other.data), fillvalue='0'):
            print(f'a={a}, b={b}')
            digit_sum = int(a, 16) + int(b, 16) + addit
            result.appendleft(f"{digit_sum % 16:X}")
            addit = digit_sum // 16
        if addit > 0:
            result.appendleft(f"{addit % 16:X}")
        return result

    def __str__(self):
        return "".join(self.data)


if __name__ == '__main__':
    data1 = HexNum('ffff')
    data2 = HexNum('ffff')
    print(data1 + data2)
