from itertools import count, cycle


counter = 0
for i in cycle('123'):
    if counter > 15:
        break
    print(i)
    counter += 1


for i in count(7):
    if i > 10:
        break
    print(i)


var = '123'
for i in count():
    if i >= 3:
        break
    for number, j in enumerate(cycle(var)):
        if number > len(var)-1:
            break
        print(j)
