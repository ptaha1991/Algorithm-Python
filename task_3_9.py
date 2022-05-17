# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random

N = 4
a = []
for i in range(N):
    b = []
    for j in range(N):
        b.append(int(random() * 100))
    a.append(b)

for i in a:
    for j in i:
        print(f'{j}'.ljust(5), end=' ')
    print()

max_el = None
for i in range(N):
    min_el = None
    for j in range(N):
        if min_el is None or a[j][i] < min_el:
            min_el = a[j][i]
    if max_el is None or min_el > max_el:
        max_el = min_el

print(max_el)
