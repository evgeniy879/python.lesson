is_bool = True
file = open('text.txt', 'w')
counter = 1
while is_bool:
    text = input(f'ввод значения для {counter} строки ')
    if not text:
        is_bool = False
        continue
    else:
        file.write(f'{text}\n')
        counter += 1
        continue
else:
    file.close()



