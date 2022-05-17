# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

n = [randint(-10, 10) for _ in range(20)]
print(n)
min_max_el = 0
for i in n:
    if min_max_el == 0 and i < 0 or min_max_el < i < 0:
        min_max_el = i

if min_max_el >= 0:
    print("В массиве нет отрицательных элементов")
else:
    print(f"Максимальный отрицательный элемент: {min_max_el}\nЕго индекс в массиве: {n.index(min_max_el)}")
