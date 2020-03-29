class Equipment:
    def __init__(self, price, quantity, brand):
        self.price = price
        self.quantity = quantity
        self.brand = brand

    def __repr__(self):
        return f'оборудование стоимостью {self.price} руб. в количестве {self.quantity} шт. типа {self.brand}'


class Xerox(Equipment):
    def __init__(self, price, quantity, brand, color, type_print):
        super().__init__(price, quantity, brand)
        self.color = color
        self.type_print = type_print

    def __repr__(self):
        param = Equipment.__repr__(self)
        return f'{param} цвета {self.color} и типом печати {self.type_print}'


class Scanner(Equipment):
    def __init__(self, price, quantity, brand, dpi, formatt):
        super().__init__(price, quantity, brand)
        self.dpi = dpi
        self.formatt = formatt

    def __repr__(self):
        param = super().__repr__()
        return f'{param} с разрешением {self.dpi} и формата {self.formatt}'


class Printer(Equipment):
    def __init__(self, price, quantity, brand, numbers_color, speed):
        super().__init__(price, quantity, brand)
        self.numbers_color = numbers_color
        self.speed = speed

    def __repr__(self):
        param = super().__repr__()
        return f'{param} количеством цветов {self.numbers_color} и скоростью печати {self.speed}'
