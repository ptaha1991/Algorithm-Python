# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

n = [randint(-10, 10) for _ in range(20)]
print(n)
ind_1 = n.index(max(n))
ind_2 = n.index(min(n))
sum_1 = 0
if ind_1 > ind_2:
    ind_1, ind_2 = ind_2, ind_1
for i in range(ind_1 + 1, ind_2):
    sum_1 += n[i]
print(sum_1)
