# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

Company = collections.namedtuple('Company', ['name', 'quarters', 'profit'])
list_companies = []
Q = 4
n = int(input("Введите количество преприятий: "))
all_profit = 0

for i in range(n):
    name = input("Наименование предприятия: ")
    quarters = []
    profit = 0
    for j in range(Q):
        quarters.append(int(input(f'Прибыль {j + 1} квартал: ')))
        profit += quarters[j]
        all_profit += quarters[j]
    list_companies.append(Company(name=name, quarters=quarters, profit=profit))

average_profit = round(all_profit / n)
print(f"Средняя прибыль за год для всех предприятий: {average_profit}")

companies_below_average_profit = []
companies_above_average_profit = []
for i in range(n):
    if list_companies[i].profit < average_profit:
        companies_below_average_profit.append(list_companies[i].name)
    elif list_companies[i].profit > average_profit:
        companies_above_average_profit.append(list_companies[i].name)
print(f"Прибыль выше среднего у следующих предприятий: {companies_above_average_profit}")
print(f"Прибыль ниже среднего у следующих предприятий: {companies_below_average_profit}")
