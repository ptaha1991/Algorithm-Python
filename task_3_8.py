# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна
# вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

N = 4
M = 4
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(input(f"Введите {j + 1} элемент {i + 1} строки: ")))
    b.append(sum(b))
    a.append(b)

for i in a:
    print(*i)
