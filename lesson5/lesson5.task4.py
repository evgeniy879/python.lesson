my_file = open('one_two_three_four.txt', mode='r', encoding='utf-8')
my_file_write = open('change_one_two_three_four.txt', 'w')

for line in my_file:
    data = line.split()
    number_letter, gap, number = map(str, data[:])
    if number_letter == 'One':
        number_letter = 'Один'
        my_file_write.write(f'{number_letter} {gap} {number}\n')
    if number_letter == 'Two':
        number_letter = 'Два'
        my_file_write.write(f'{number_letter} {gap} {number}\n')
    if number_letter == 'Three':
        number_letter = 'Три'
        my_file_write.write(f'{number_letter} {gap} {number}\n')
    if number_letter == 'Four':
        number_letter = 'Четыре'
        my_file_write.write(f'{number_letter} {gap} {number}\n')
my_file.close()
my_file_write.close()
