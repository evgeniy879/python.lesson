from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def add_items(self):
        pass

    @abstractmethod
    def items_off(self):
        pass

    @abstractmethod
    def show_info(self):
        pass


class Storage(AbstractStorage):
    __count = 0

    def __init__(self):
        self.__is_storage_empty = 'Empty'
        self.__values = {'принтер': 1000, 'ксерокс': 1500, 'сканер': 500}
        self.__deals = {'принтер': {'quantity': [0], 'price': [0]}, 'ксерокс': {'quantity': [0], 'price': [0]},
                        'сканер': {'quantity': [0], 'price': [0]}}
        Storage.__count += 1

# добавление товара на скад
    def add_items(self, type_, quantity):
        self.__is_storage_empty = 'not empty'
        if type(quantity) == str:
            print('Ввод только числовых данных')
        else:
            for i in self.__deals:
                if i == type_:
                    self.__deals[i]['quantity'].append(quantity)
                    val = quantity * self.__values[type_]
                    self.__deals[i]['price'].append(val)

# списание со склада товара в подразделение компании
    def items_off(self, type_, quantity):
        counter = 0
        if self.__is_storage_empty == 'not empty':
            for i in self.__deals:
                if i == type_:
                    sum_q = sum(self.__deals[i]['quantity'])
                    if sum_q >= quantity:
                        val = quantity * self.__values[type_]
                        self.__deals[i]['quantity'].append(-quantity)
                        self.__deals[i]['price'].append(-val)
                    else:
                        print('на скаде не имеется достаточного количества товара')
        else:
            print(f'данного количества товара нет на скаде')
        for i in self.__deals:
            if sum(self.__deals[i]['quantity']) > 0:
                counter += 1
        if counter == 0:
            self.__is_storage_empty = 'Empty'
        else:
            self.__is_storage_empty = 'not empty'

# информация по наличию товара на складе
    def show_info(self):
        for i in self.__deals:
            sum_q = sum(self.__deals[i]['quantity'])
            sum_p = sum(self.__deals[i]['price'])
            print(f'количество {i}ов на складе составляет {sum_q} шт на общую сумму {sum_p} руб.')

# состояния переменных
    def get_storage(self):
        return f'Склад {self.__is_storage_empty}'

    state = property(get_storage)

    def get_values(self):
        return f'Установленные цены на оргтехнику {self.__values}'

    values = property(get_values)

    @property
    def deals(self):
        return self.__deals

    @classmethod
    def count_storage(cls):
        return f'экземпляров класса создано в количестве {cls.__count} шт.'

obj = Storage()
print(Storage.count_storage())
obj.add_items('принтер', 5)
obj.add_items('сканер', 1)
obj.add_items('ксерокс', 2)
obj.items_off('принтер', 5)
obj.items_off('принтер', 5)
obj.show_info()
