def func_counter():
    n = input().split()
    sum = 0
    is_continue = True
    while is_continue:
        if 'Q' in n:
            for i in n:
                if i == 'Q':
                    is_continue = False
                    continue
                else:
                    sum += int(i)
            is_continue = False
            continue
        for i in n:
            sum += int(i)
        print(sum)
        n = input().split()
        continue
    else:
        return(sum)


print(func_counter())
