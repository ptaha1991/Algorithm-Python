# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def middle_number(n1, n2, n3):
    if n2 < n1 < n3 or n3 < n1 < n2:
        return n1
    elif n1 < n2 < n3 or n3 < n2 < n1:
        return n2
    else:
        return n3


if __name__ == '__main__':
    print(middle_number(
        int(input()),
        int(input()),
        int(input())
    ))
