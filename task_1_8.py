# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

def type_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Високосный год')
    else:
        print('Невисокосный год')


if __name__ == '__main__':
    type_year(int(input()))
