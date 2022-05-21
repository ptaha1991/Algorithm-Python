# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Проанализировать скорость и сложность алгоритмов.
from time import time

n = 10000

# Используя алгоритм «Решето Эратосфена» (методичка) - сложность O(nloglogn)
start1 = time()
a = [i for i in range(n + 1)]
a[1] = 0
m = 2
while m < n:
    if a[m] != 0:
        j = m * 2
        while j <= n:
            a[j] = 0
            j = j + m
    m += 1
b = []
for i in a:
    if a[i] != 0:
        b.append(a[i])
del a
print(b)
end1 = time()

# Используя алгоритм «Решето Эратосфена» (вебинар) - сложность O(nloglogn)
start2 = time()
sieve = set(range(2, n + 1))
prime_set = []
while sieve:
    prime = min(sieve)
    prime_set.append(prime)
    sieve -= set(range(prime, n + 1, prime))
print(prime_set)
end2 = time()

# Мой вариант Сложность O(n**2) (Квадратичная)
start3 = time()
my_prime_set = []
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        my_prime_set.append(i)
print(my_prime_set)
end3 = time()

print(end1 - start1, 'c')
print(end2 - start2, 'c')
print(end3 - start3, 'c')

# При n = 100000
# 1ый вариант  0.09373593330383301 c
# 2ой вариант  3.4202234745025635 c
# 3ий вариант  46.34580326080322 c
# Естественно, что третий вариант очень сильно проигрывает в скорости.
# Могу предположить, что разность сетов(второй вариант) имеет большую сложность,
# чем проход циклом while и присваивание нулей(первый вариант)
