my_list = [7, 5, 3, 3, 2]
number = int(input())

if number in my_list:
    index = my_list.index(number)
    my_list.insert(index, number)
if number not in my_list:
    for i in my_list:
        if i > number:
            continue
        else:
            index = my_list.index(i)
            my_list.insert(index, number)
            break
if number < my_list[-1]:
    my_list.append(number)
print(my_list)
