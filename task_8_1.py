# 1. 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.


import hashlib


def sum_substring(st):
    n = len(st)
    sum_substr = set()
    for i in range(n):
        for j in range(n, i, -1):
            hash_str = hashlib.sha1(st[i:j].encode('utf-8')).hexdigest()
            sum_substr.add(hash_str)
    return len(sum_substr) - 1


if __name__ == '__main__':
    print(sum_substring(input('Введите строку, состоящую только из маленьких латинских букв: ')))




