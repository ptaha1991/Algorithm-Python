# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
from random import randint
from time import time


def random_array(n):
    a = [randint(-100, 99) for _ in range(n)]
    return a


def bubble_sort(nums):
    nums = nums[:]
    swapped = False
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] < nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return nums


def cocktail_sort(nums):
    nums = nums[:]
    n = len(nums)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for j in range(end - 1, start - 1, -1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        start = start + 1
    return nums


if __name__ == '__main__':
    b = random_array(1000)
    print(b)
    start1 = time()
    print(bubble_sort(b))
    end1 = time()
    start2 = time()
    print(cocktail_sort(b))
    end2 = time()
    print(end1 - start1, 'c - скорость работы 1ого варианта')
    print(end2 - start2, 'c - скорость работы 2ого варианта')

# Временная сложность - O(n**2) Квадратичная
# Пространственная сложность - O(n) Линейная - в моем случае, так как чтобы реализовать 2 варианта, нужно было сделать
# копию массива, но в обычном случае это сортировка на месте - то есть сложность O(1)
# при n = 10000
# 7.739566326141357 c - скорость работы 1ого варианта
# 6.659823656082153 c - скорость работы 2ого варианта
