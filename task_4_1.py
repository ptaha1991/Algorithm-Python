# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных
# в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# 3_4. Определить, какое число в массиве встречается чаще всего.

from random import randint
from time import time

a = [randint(0, 10) for i in range(10000)]
print(a)

# 1ый вариант через словарь
# Сложность линейнаяO(n)
# Могу предположить, что 1 действие  - это O(n), 2 - O(n), 3 - O(1), 4 - O(n), 5 - O(1). В сумме O(3n), тройка не важна
start1 = time()
b = dict.fromkeys(a, 0)  # 1
for i in a:  # 2
    b[i] += 1  # 3
max_n = max(b, key=b.get)  # 4
print(f"Число {max_n} встречается {b[max_n]} раз(а) ")  # 5
end1 = time()

# 2ой вариант через новый список
# Сложность линейная O(n)
# O(1) + O(n) + O(1) + O(n) + O(n) + O(1) = O(3n)
start2 = time()
a_frq = []  # 1
for i in a:  # 2
    a_frq.append(a.count(i))  # 3 и 4
max_frq = max(a_frq)  # 5
print(f"Число {a[a_frq.index(max_frq)]} встречается {max_frq} раз(а)")  # 6
end2 = time()

# 3ий вариант через вложенный цикл
# Здесь важно, что присутсвует вложенный цикл, а значит это уже O(n**2) (Квадратичная)
start3 = time()
max_n2 = a[0]
max_frq2 = 1
for i in range(len(a)):
    frq = 1
    for k in range(i + 1, len(a)):
        if a[i] == a[k]:
            frq += 1
    if frq > max_frq:
        max_frq2 = frq
        max_n2 = a[i]
print(f"Число {max_n2} встречается {max_frq2} раз(а)")
end3 = time()

print(end1 - start1, 'c - скорость работы 1ого варианта')
print(end2 - start2, 'c - скорость работы 2ого варианта')
print(end3 - start3, 'c - скорость работы 3ого варианта')
