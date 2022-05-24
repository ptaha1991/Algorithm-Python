# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
import collections

hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def number_to_deque(n):
    deq_numb = collections.deque(n.upper())
    return deq_numb


def sum_hex(n1, n2):
    if type(n1) and type(n2) is str:
        n1 = number_to_deque(n1)
        n2 = number_to_deque(n2)
    if len(n1) < len(n2):
        n1.extendleft('0' * (len(n2) - len(n1)))
    elif len(n1) > len(n2):
        n2.extendleft('0' * (len(n1) - len(n2)))
    sum_result = collections.deque()
    temp = 0
    for i in range(len(n1) - 1, -1, -1):
        sum_elements = hex_list.index(n1[i]) + hex_list.index(n2[i]) + temp
        if sum_elements < len(hex_list):
            temp = 0
        else:
            temp = 1
            sum_elements -= len(hex_list)
        sum_result.appendleft(hex_list[sum_elements])
    if temp == 1:
        sum_result.appendleft('1')
    return sum_result


def mul_hex(n1, n2):
    if type(n1) and type(n2) is str:
        n1 = number_to_deque(n1)
        n2 = number_to_deque(n2)
    mul_result = collections.deque('0')
    depth = 0
    for i in range(len(n2) - 1, -1, -1):
        temp = 0
        result_mul_elements = collections.deque()
        for j in range(len(n1) - 1, -1, -1):
            mul_elements = hex_list.index(n2[i]) * hex_list.index(n1[j]) + temp
            if mul_elements < len(hex_list):
                temp = 0
            else:
                temp = mul_elements // len(hex_list)
                mul_elements %= len(hex_list)
            result_mul_elements.appendleft(hex_list[mul_elements])
        if temp > 0:
            result_mul_elements.appendleft(hex_list[temp])
        for d in range(depth):
            result_mul_elements.append('0')
        depth += 1
        mul_result = sum_hex(mul_result, result_mul_elements)
    return mul_result


if __name__ == '__main__':
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    print(sum_hex(a, b))
    print(mul_hex(a, b))

    a = list(a)
    b = list(b)
# 2ой вариант
    sum_hex1 = hex(int(''.join(a), 16) + int(''.join(b), 16)).split('0x')[1]
    mul_hex1 = hex(int(''.join(a), 16) * int(''.join(b), 16)).split('0x')[1]
    print(list(sum_hex1), list(mul_hex1))
# 3ий вариант
    sum_hex2 = format(int(''.join(a), 16) + int(''.join(b), 16), 'x')
    mul_hex2 = format(int(''.join(a), 16) * int(''.join(b), 16), 'x')
    print(list(sum_hex2), list(mul_hex2))
