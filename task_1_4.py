# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
import random


def random_symbol_in_limits(random_type, start, stop):
    if random_type == 'i':
        return random.randint(int(start), int(stop))
    elif random_type == 'f':
        return random.uniform(int(start), int(stop))
    elif random_type == 's':
        return chr(random.randint(ord(start), ord(stop)))
    raise Exception('Введен не верный random_type')


if __name__ == '__main__':
    print(random_symbol_in_limits(
        input(),
        input(),
        input()
    ))
