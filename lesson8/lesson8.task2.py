class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

user_data = int(input('введите число: '))

try:
    if user_data == 0:
        raise OwnError('Число не должно равняться нулю')
    else:
        result = 100 / user_data
except OwnError as err:
        print(err)
else:
    print(f'результат деления {result}')

