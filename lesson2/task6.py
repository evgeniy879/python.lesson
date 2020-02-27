new_list= []
var_bool = True
counter = 1

while var_bool:
    goods = {'название': [], 'цена': [], 'количество': [], 'eд': []}
    for i in goods:
        if i == 'название':
            goods[i].append(input('введите название техники: '))
        if i == 'цена':
            goods[i].append(int(input('укажите цену: ')))
        if i == 'количество':
            goods[i].append(int(input('укажите количество: ')))
        if i == 'eд':
            goods[i].append(input('укажите в чем измеряется: '))
    new_tuple = (counter, goods)
    new_list.append(new_tuple)
    question = input('продолжить ввод данных: да/нет ')
    if question == 'нет':
        var_bool = False
        continue
    else:
        counter += 1
        continue
else:
    print(new_list)
