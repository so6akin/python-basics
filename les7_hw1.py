# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4. Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
# в привычном виде. Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица. Подсказка: сложение элементов
# матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом
# первой строки второй матрицы и т.д.

from copy import deepcopy


class Matrix:

    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                amount = self.matrix[i][j] + other.matrix[i][j]
                numbers.append(amount)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


matrix1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
matrix2 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
matrix3 = matrix1 + matrix2
print(matrix3)
