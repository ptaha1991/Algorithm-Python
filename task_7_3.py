# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

from random import randint
from time import time


def find_median_without_sorting(nums):
    median_ind = 0
    for i in range(len(nums)):
        more_count = 0
        less_count = 0
        equal_count = 0
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[j] < nums[i]:
                more_count += 1
                if more_count > len(nums) // 2:
                    break
            elif nums[j] > nums[i]:
                less_count += 1
                if less_count > len(nums) // 2:
                    break
            elif nums[j] == nums[i]:
                equal_count += 1
        while equal_count > 0:
            if more_count < less_count:
                more_count += 1
            else:
                less_count += 1
            equal_count -= 1
        if more_count == less_count:
            median_ind = nums[i]
            break
    return median_ind


def gnome_sort(nums):
    nums = nums[:]
    index = 1
    i = 0
    n = len(nums)
    while i < n - 1:
        if nums[i] <= nums[i + 1]:
            i, index = index, index + 1
        else:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i = i - 1
            if i < 0:
                i, index = index, index + 1
    median = nums[len(nums) // 2]
    return median


if __name__ == '__main__':
    m = 1000
    a = [randint(0, 100) for i in range(2 * m + 1)]
    print(a)

    start1 = time()
    print(find_median_without_sorting(a))
    end1 = time()

    start2 = time()
    print(gnome_sort(a))
    end2 = time()

    start3 = time()
    a.sort()
    print(a[len(a) // 2])
    end3 = time()

    print(end1 - start1, 'c - скорость работы 1го варианта')
    print(end2 - start2, 'c - скорость работы 2го варианта')
    print(end3 - start3, 'c - скорость работы 3го варианта')

# 1ый вариант: find_median_without_sorting
# Временная сложность - O(n**2) Квадратичная
# Пространственная сложность - O(1)
# 2ой вариант: gnome_sort
# Временная сложность - O(n**2) Квадратичная
# Пространственная сложность - O(1)
# 3ий вариант: a.sort()
# Временная сложность - O (nlog (n))
# Пространственная сложность - O(1)
# При n = 10000:
# 0.4098670482635498 c - скорость работы 1го варианта
# 32.433478116989136 c - скорость работы 2го варианта
# 0.0019996166229248047 c - скорость работы 3го варианта
