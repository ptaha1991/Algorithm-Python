# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


def sum_and_product_number(n):
    a = n % 10
    b = n % 100 // 10
    c = n // 100
    return f"Сумма цифр числа: {a + b + c}\nПроизведение цифр числа: {a * b * c}"


if __name__ == '__main__':
    print(sum_and_product_number(int(input("Введите трехзначное число: "))))
