# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.


if __name__ == '__main__':
    x1 = int(input("Введите координату x1: "))
    y1 = int(input("Введите координату y1: "))
    x2 = int(input("Введите координату x2: "))
    y2 = int(input("Введите координату y2: "))

    A = y1 - y2
    B = x2 - x1
    if A == 0 or B == 0:
        print("Введены некорректные координаты")
        exit(1)
    C = x1 * y2 - x2 * y1
    print(f"{A}x", end='')
    if B > 0:
        print(f' + {B}y', end='')
    else:
        print(f' - {abs(B)}y', end='')
    if C > 0:
        print(f' + {C}', end='')
    elif C < 0:
        print(f' - {abs(C)}', end='')
    print(' = 0')
