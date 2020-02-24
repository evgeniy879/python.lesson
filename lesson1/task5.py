cost = int(input('введите сумму издержек '))
revenues = int(input('введите сумму выручки '))
profit = revenues - cost
if profit > 0:
    print(f'прибыль фирмы составила {profit}')
    profitability = profit / revenues
    count_workers = int(input('введите число сотрудников '))
    profit_per_count_workers = profit / count_workers
    print(f'прибыль из расчета на одного сотрудника фирмы составляет {profit_per_count_workers}')
else:
    print(f'убыток фирмы составил {profit}')
