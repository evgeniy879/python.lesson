from random import randint

list_number = [randint(1, 20) for i in range(5)]

my_file = open('sum_number.txt', 'w')
for i in list_number:
    my_file.write(f'{i} ')
my_file.close()

my_file = open('sum_number.txt', 'r')
sum = 0
content = my_file.read()
data = content.split()
for i in data:
    sum += int(i)
print(sum)
my_file.close()
