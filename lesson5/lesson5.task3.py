with open('workers.txt', encoding='utf-8') as file:
    average_income = 0
    counter_staff = 0
    for line in file:
        data = line.split()
        sum_workers = float(data[1])
        average_income += sum_workers
        counter_staff += 1
        if sum_workers < 20000:
            print(f'фамилия сотрудника, чей доход меньше 20тыс: {data[0]}')
    print(f'средний доход сотрудников соствляет {average_income / counter_staff}')
