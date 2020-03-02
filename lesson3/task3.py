def my_func(a, b, c):
    if min(min(a, b), c) == c:
        return (a + b)
    if min(min(a, b), c) == b:
        return (a + c)
    if min(min(a, b), c) == a:
        return (b + c)


print(my_func(3, 1, 4))
