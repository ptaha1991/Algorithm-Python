# 3_9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random
from sys import getsizeof

# Создание и вывод матрицы
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

# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
max_el = None
for i in range(N):
    min_el = None
    for j in range(N):
        if min_el is None or a[j][i] < min_el:
            min_el = a[j][i]
    if max_el is None or min_el > max_el:
        max_el = min_el

print(max_el)
print('Переменные занимают', getsizeof(max_el) + getsizeof(min_el), 'б')
# Временная сложность - O(n**2) Квадратичная, так как имеем вложенный цикл по N.
# Пространственная сложность - O(1) Константная
# В решении мы храним только 2 переменные значения которых меняются в ходе выполнения цикла.
# Наверное, если оформить код в виде функции мы избавимся от хранения переменной min_el.
# Что в целом все равно никак не повлияет на пространственную сложность
