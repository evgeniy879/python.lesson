class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(round(self.number / other.number))

    def __str__(self):
        return str(self.number)

    def __sub__(self, other):
        result = self.number - other.number
        if result > 0:
            return result
        else:
            return f'Вычитание невозможно'

    def make_order(self, number_in_row):
        self.number_in_row = number_in_row
        sum = 0
        print_row_times, print_in_row = self.number // number_in_row, self.number % number_in_row
        while sum < print_row_times:
            for i in range(number_in_row):
                print('*', end='')
            sum += 1
            print()
        for i in range(print_in_row):
            print('*', end='')
        print()



cell_1 = Cell(9)
cell_2 = Cell(5)

cell_1.make_order(8)
print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1 - cell_2)