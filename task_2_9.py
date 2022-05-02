# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def sum_digits_n(n):
    sum_digits = 0
    for digit in n:
        sum_digits += int(digit)
    return sum_digits


def max_number_by_sum_digits(list_number):
    max_number = 0
    max_sum = 0
    for i in list_number:
        if sum_digits_n(i) > max_sum:
            max_number = i
            max_sum = sum_digits_n(i)
    print(f'Наибольшая сумма цифр {max_sum} у числа {max_number}')


if __name__ == '__main__':
    max_number_by_sum_digits(
        [i for i in input('Введите натуральные числа через пробел: ').split()]
    )
    