# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint
from time import time

n = [randint(-10, 10) for _ in range(200000)]
print(n)

# 1ый способ
start1 = time()
ind_min_1 = n.index(min(n))
min_2 = min(n[:ind_min_1] + n[ind_min_1 + 1:])
print(n[ind_min_1], min_2)
end1 = time()

# 2ой способ
start2 = time()
b = sorted(n)
print(b[0], b[1])
end2 = time()

# 3ий способ
start3 = time()
min1 = min(n)
n.remove(min1)
min2 = min(n)
print(min1, min2)
end3 = time()

print(end1 - start1, 'c')
print(end2 - start2, 'c')
print(end3 - start3, 'c')
