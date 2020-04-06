import json


firms = []
dict_firms = {}
dict_aver_income = {'average_profit': 0}
sum, counter = 0, 0

with open('firms.txt', encoding='utf-8') as my_file:
    for line in my_file:
        firm = line.split()[0]
        revenue, cost = int(line.split()[-2]), int(line.split()[-1])
        income = revenue - cost
        dict_firms[firm] = income
        if income > 0:
            sum += int(income)
            counter += 1
aver_income = sum / counter

dict_aver_income['average_profit'] = aver_income
firms.append(dict_firms)
firms.append(dict_aver_income)

with open('my_file.json', 'w') as f:
    json.dump(firms, f, indent=2, ensure_ascii=False)


my_file = open('my_file.json')
content = my_file.read()
print(content)
my_file.close()
