class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row_str = ''

    def __str__(self):
        for i in self.matrix:
            self.row_str += '  '.join(map(str, i)) + '\n'
        return self.row_str

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.matrix)):
            temp = []
            for j in range(len(self.matrix[0])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                temp.append(summa)
            new_matrix.append(temp)
        return Matrix(new_matrix)


my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_1 = Matrix(my_list)
m_2 = Matrix(my_list)
print(m_1)
print(m_1 + m_2)
