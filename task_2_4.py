# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов
# (n) вводится с клавиатуры.

def sum_elements(n):
    sum_n = 0
    a = 1
    while n > 0:
        sum_n += a
        a /= -2
        n -= 1
    return sum_n


if __name__ == '__main__':
    print(sum_elements(int(input())))
