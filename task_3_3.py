# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

a = [randint(0, 99) for i in range(20)]
print(a)
index_max_a = a.index(max(a))
index_min_a = a.index(min(a))
a[index_min_a], a[index_max_a] = a[index_max_a], a[index_min_a]
print(a)
