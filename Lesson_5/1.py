"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import namedtuple, OrderedDict, Counter


def quarter_data(start=0):
    while start < 4:
        yield int(input(f"Введите прибыль предприятия за {start + 1}-й квартал: "))
        start += 1


def get_data():
    count = int(input("Введите количество предприятий: "))
    data = OrderedDict()
    quarters = namedtuple("Quarters", "first second third forth")
    for i in range(1, count + 1):
        name = input(f"Введите наменование предприятия {i}: ")
        data[name] = quarters(*(i for i in quarter_data()))
    return data


if __name__ == '__main__':
    data = get_data()
    avg_revenue = sum(sum(i) for i in data.values())/len(data)

    above_avg = list()
    under_avg = list()
    for key, value in data.items():
        if sum(value) > avg_revenue:
            above_avg.append(key)
        elif sum(value) < avg_revenue:
            under_avg.append(key)

    nl = '\n'
    print(f"Предприятия с прибылью выше среднего:{nl}{nl.join(above_avg)}")
    print(f"Предприятия с прибылью ниже среднего:{nl}{nl.join(under_avg)}")
