# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не
# должна завершаться, а должна запрашивать новые данные для вычислений. Завершение
# программы должно выполняться при вводе символа '0' в качестве знака операции. Если
# пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об
# ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности
# деления на ноль, если он ввел 0 в качестве делителя

def arithmetic_operations():
    try:
        n1 = float(input('Введите первое число: '))
        n2 = float(input('Введите второе число: '))
    except ValueError:
        print('Число введено не верно. Попробуйте снова')
        return arithmetic_operations()
    while True:
        op = input('Введите знак операции или 0 для отмены: ')
        if op == '0':
            print("Завершение программы")
            return
        elif op == '+':
            print(f'{n1} {op} {n2} = {n1 + n2}')
            return arithmetic_operations()
        elif op == '-':
            print(f'{n1} {op} {n2} = {n1 - n2}')
            return arithmetic_operations()
        elif op == '*':
            print(f'{n1} {op} {n2} = {n1 * n2}')
            return arithmetic_operations()
        elif op == '/':
            try:
                print(f'{n1} {op} {n2} = {n1 / n2}')
            except ZeroDivisionError:
                print('На ноль делить нельзя')
            return arithmetic_operations()
        else:
            print('Ошибка. Нет такой команды')


if __name__ == '__main__':
    arithmetic_operations()
