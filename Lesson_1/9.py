# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).


if __name__ == '__main__':
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))

    if a == b or b == c or a == c:
        print("Введены одинаковые числа")
        exit(1)

    print("Среднее число: ", end='')
    if a > b:
        if b > c:
            print(b)
        else:
            if c > a:
                print(a)
            else:
                print(c)
    else:
        if b < c:
            print(b)
        else:
            if c < a:
                print(a)
            else:
                print(c)