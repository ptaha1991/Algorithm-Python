# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

def equation_of_straight_line(x1, y1, x2, y2):
    k = (y2 - y1)/(x2 - x1)
    b = y1 - k * x1
    return f'Уравнение прямой: y = {k:0.2f}x + {b:0.2f}'


if __name__ == '__main__':
    print(equation_of_straight_line(
        int(input()),
        int(input()),
        int(input()),
        int(input())))
