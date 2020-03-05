my_list = [2, 3, 4, 2, 5, 1, 3, 5, 4, 8, 9, 2]
new_list = [x for x in my_list if my_list.count(x) == 1]
print(new_list)
