def fact(n):
    new_list = [x for x in range(1, n+1)]
    sum = 1
    for i in new_list:
        sum *= i
        yield sum


factorial = fact(5)
for i in factorial:
    print(i)
