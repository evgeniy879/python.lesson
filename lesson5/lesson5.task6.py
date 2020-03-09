dict_study = {}

with open('study.txt', encoding='utf-8') as my_file:
    for line in my_file:
        subject = line.strip().split(' ')[0][:-1]
        data = line.strip().split(' ')[1:]
        number_data = []
        for i in data:
            None if i == '-' else number_data.append(i)
        sum = 0
        for i in number_data:
            sum += int(i.split('(')[0])
        dict_study[subject] = sum

print(dict_study)
