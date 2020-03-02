def func_div(number1, number2):
    try:
        result = number1 / number2
        return result
    except ZeroDivisionError:
        print('Попытка деления на 0')


number1 = int(input('Введите число '))
number2 = int(input('Введите число '))

print(func_div(number1, number2))
