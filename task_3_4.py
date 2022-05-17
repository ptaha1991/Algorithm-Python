# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

a = [randint(0, 9) for i in range(20)]
print(a)
b = dict.fromkeys(a, 0)
for i in a:
    b[i] += 1
print(b)
max_n = max(b, key=b.get)
print(f"Число {max_n} встречается {b[max_n]} раз(а) ")
