class OwnError(Exception):
    def __init__(self, param):
        self.txt = param


try:
    sum = 0
    is_bool = True
    while is_bool:
        data = input('Ввод значений через пробел: ').split()
        for i in data:
            if i == 'stop':
                is_bool = False
                continue
            elif i not in '0123456789':
                raise OwnError('Ввод только чисел')
            elif i != 'stop':
                sum += int(i)
        print(sum)
except OwnError as err:
    print(err)

