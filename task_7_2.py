# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import uniform


def random_array(n):
    a = [round(uniform(0, 50), 2) for i in range(n)]
    return a


def merge(left, right):
    sorted_list = []
    left_id = right_id = 0
    while left_id < len(left) and right_id < len(right):
        if left[left_id] <= right[right_id]:
            sorted_list.append(left[left_id])
            left_id += 1
        else:
            sorted_list.append(right[right_id])
            right_id += 1
    if left_id < len(left):
        sorted_list += left[left_id:]
    if right_id < len(right):
        sorted_list += right[right_id:]
    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


if __name__ == '__main__':
    b = random_array(1000)
    print(b)
    print(merge_sort(b))

# Временная сложность - O(nlog(n)) Квадратичная
# Пространственная сложность - O(n) Линейная
