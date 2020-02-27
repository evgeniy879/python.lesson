new_list = input().split()
for i in range(len(new_list)):
    new_list[i] = int(new_list[i])
list_change = []

if len(new_list) % 2 == 0:
    for i in range(len(new_list)):
        if i % 2 == 0:
            list_change.append(new_list[i-len(new_list)+1])
            list_change.append(new_list[i-len(new_list)])
if len(new_list) % 2 != 0:
    for i in range(len(new_list)-1):
        if i % 2 == 0:
            list_change.append(new_list[i-len(new_list)+1])
            list_change.append(new_list[i-len(new_list)])
    list_change.append(new_list[-1])
print(list_change)
