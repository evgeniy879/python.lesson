def my_func1(x, y):
    return x ** y


print(my_func1(2, -1))


def my_func2(x, y):
    result = 1
    while y < 0:
        result *= x
        y += 1
    return 1 / result


print(my_func2(2, -1))
