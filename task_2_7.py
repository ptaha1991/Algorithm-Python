# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных
# чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def expression1(n):
    if n == 1:
        return n
    elif n > 0:
        return n + expression1(n-1)


def expression2(n):
    return n * (n + 1) // 2


def equality_check(n):
    if expression1(n) == expression2(n):
        print(f'1+2+...+{n} = {n}({n}+1)/2\n{expression1(n)} = {expression2(n)}\nРавенство выполняется')
    else:
        print(f'Равенство 1+2+...+n = n(n+1)/2, где n = {n}  не выполняется. Возможно вы ввели не натуральное число')


if __name__ == '__main__':
    equality_check(int(input()))

