class ComplexNumbers:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def __add__(self, other):
        result = ComplexNumbers(self.param_1 + other.param_1, self.param_2 + other.param_2)
        return result

    def __mul__(self, other):
        result_1 = self.param_1 * other.param_1 - self.param_2 * other.param_2
        result_2 = self.param_1 * other.param_2 + other.param_1 * self.param_2
        return ComplexNumbers(result_1, result_2)

    def __str__(self):
        return f'{self.param_1} + {self.param_2}i'

obj = ComplexNumbers(2, 3)
print(obj)

obj1 = ComplexNumbers(2, 3)
obj2 = ComplexNumbers(2, 3)
print(obj1 * obj2)
print(obj1 + obj2)
