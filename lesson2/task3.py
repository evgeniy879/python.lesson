number = int(input())
new_list = [None, 'зима', 'зима', 'весна','весна','весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(new_list[number])
new_dict = {'зима': [1, 2, 12], 'лето': [6, 7, 8], 'осень': [9, 10, 11], 'весна': [3, 4, 5]}
number = int(input())
for i in new_dict:
    for j in new_dict[i]:
        if j == number:
            print(i)
