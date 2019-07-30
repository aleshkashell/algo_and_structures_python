"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""


def is_exist(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    return False


def is_isosceles(a, b, c):
    if a == b or b == c or a == c:
        return True
    return False


def is_equilateral(a, b, c):
    if a == b == c:
        return True
    return False


def is_acute(a, b, c):
    if a < b:
        if b < c:
            hypotenuse = c
            leg_1 = a
            leg_2 = b
        else:
            hypotenuse = b
            leg_1 = a
            leg_2 = c
    else:
        if a < c:
            hypotenuse = c
            leg_1 = a
            leg_2 = b
        else:
            hypotenuse = a
            leg_1 = b
            leg_2 = c

    if hypotenuse**2 < leg_1**2 + leg_2**2:
        print("имеет острые углы")
    elif hypotenuse**2 > leg_1**2 + leg_2**2:
        print("имеет тупой угол")
    else:
        print("имеет прямой угол")


if __name__ == '__main__':
    a = int(input("Введите первую сторону: "))
    b = int(input("Введите вторую сторону: "))
    c = int(input("Введите третью сторону: "))

    if not is_exist(a, b, c):
        print("Такого треугольника не существует")
        exit(0)
    if is_equilateral(a, b, c):
        print("Это равносторонний треугольник")
        exit(0)
    if is_isosceles(a, b, c):
        print("Это равнобедренный треугольник и ", end='')
    else:
        print("Треугольник существует и ", end='')
    is_acute(a, b, c)
