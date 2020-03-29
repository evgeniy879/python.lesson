class Date:
    def __init__(self, data):
        self.data = data

    @classmethod
    def int_data(cls, data):
        [print(i, end=' ') for i in [int(i) for i in data.split('-')]]

    @staticmethod
    def is_true(data):
        day, month, year = [int(i) for i in data.split('-')]
        day_bool = True if (day < 32 and day > 0) else False
        month_bool = True if (month < 13 and month > 0) else False
        year_bool = True if (year < 2021 and year > 0) else False
        print(f'\nправильность ввода данных: день {day_bool}, месяц {month_bool}, год {year_bool}')

    def get_info(self):
        print(self.data)


data = '11-02-15'
date1 = Date('11-12-15')
date1.get_info()
Date.int_data(data)
Date.is_true(data)
