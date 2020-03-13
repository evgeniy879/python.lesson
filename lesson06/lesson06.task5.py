class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} пишет')


pen = Pen('Ручка')

pen.draw()


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} рисует')


pencil = Pencil('карандаш')
pencil.draw()


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} выделяет')

handle = Handle('Маркер')
handle.draw()
