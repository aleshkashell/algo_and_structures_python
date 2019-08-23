"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib


def main():
    substrings = set()
    text = input("Введите строку из маленьких латинских букв: ")
    length = len(text)
    for i in range(length):
        for j in range(i, length):
            if j + 1 - i < length:
                substrings.add(hashlib.md5(text[i:j+1].encode('utf-8')).hexdigest())

    print(f'В строке "{text}" {len(substrings)} подстрок')
    print(substrings)


if __name__ == '__main__':
    main()
