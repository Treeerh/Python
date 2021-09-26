# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
#
# Следующий шаг — реализовать перегрузку метода str()
# для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и пр.

from abc import ABC, abstractmethod


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def rang_matrix(self):
        l = len(self.matrix)
        r = len(self.matrix[0])
        return str(l) + str(r)

    def __add__(self, other):
        if self.rang_matrix() == other.rang_matrix():
            matrix = []
            for i in range(len(self.matrix)):
                temp = []
                for j in range(len(self.matrix[i])):
                    temp.append(self.matrix[i][j] + other.matrix[i][j])
                matrix.append(temp)

            return Matrix(matrix)
        else:
            return 'Matrices do not match'


m_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_1 = Matrix(m_1)
matrix_2 = Matrix(m_2)

matrix = matrix_1 + matrix_2
print(matrix)
