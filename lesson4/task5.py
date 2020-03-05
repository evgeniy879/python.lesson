from functools import reduce


def my_func(prev_a, a):
    return prev_a * a


new_list = [x for x in range(100, 1001)]
result = reduce(my_func, new_list)
print(result)
