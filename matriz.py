"""
    Arquivo Python com funcoes para manipulacao de matrizes.
"""


def identity_matrix(n: int) -> [[int]]:
    """
    Funcao que cria uma matriz identidade de ordem n.
    Retorna uma matriz.
    """
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            if i != j:
                matrix[i].append(0)
            else:
                matrix[i].append(1)

    return matrix


def transpose_matrix(matrix: [[float]]) -> [[float]]:
    """
    Funcao que retorna a transposta de uma matriz.
    Retorna uma matriz.
    """
    t_matrix = []
    for j, _ in enumerate(matrix[0]):
        t_matrix.append([])
        for i, _ in enumerate(matrix):
            t_matrix[j].append(matrix[i][j])

    return t_matrix


def sum_matrix(matrix1: [[float]], matrix2: [[float]]) -> [[float]]:
    """
    Funcao que soma duas matrizes.
    Retorna uma matriz.
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None

    matrix = []

    for i, _ in enumerate(matrix1):
        matrix.append([])
        for j, _ in enumerate(matrix1[0]):
            elem1 = matrix1[i][j]
            elem2 = matrix2[i][j]
            matrix[i].append(elem1 + elem2)

    return matrix


def subtract_matrix(matrix1: [[float]], matrix2: [[float]]) -> [[float]]:
    """
    Funcao que soma duas matrizes.
    Retorna uma matriz.
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None

    matrix = []

    for i, _ in enumerate(matrix1):
        matrix.append([])
        for j, _ in enumerate(matrix1[0]):
            elem1 = matrix1[i][j]
            elem2 = matrix2[i][j]
            matrix[i].append(elem1 - elem2)

    return matrix


def multiply_matrix(matrix1: [[float]], matrix2: [[float]]) -> [[float]]:
    """
    Funcao que multiplica duas matrizes.
    Retorna uma matriz.
    """
    if len(matrix1[0]) != len(matrix2):
        return None

    matrix = []

    for i, row in enumerate(matrix1):
        matrix.append([])
        for k, _ in enumerate(matrix2[0]):
            result = 0
            for j, val in enumerate(matrix2):
                result += row[j] * val[k]
                # print(f'a{i+1}{j+1} b{j+1}{k+1}')
            matrix[i].append(result)

    return matrix


class Matrix:
    """
    Classe Matrix
    """

    from typing import Tuple

    def __init__(self, matrix: [[float]]):
        self.matrix = matrix
        self.determinant = self._calc_determinant(self.matrix)
        self.size = (len(matrix), len(matrix[0]))

    def __getitem__(self, coords: Tuple[int, int]):
        i = coords[0]
        j = coords[1]
        try:
            return self.matrix[i][j]
        except IndexError:
            return None

    def __setitem__(self, coords: Tuple[int, int], value):
        i = coords[0]
        j = coords[1]
        try:
            self.matrix[i][j] = float(value)
        except IndexError:
            pass

    def __repr__(self) -> str:
        text = ""
        for row in self.matrix:
            text += f"{row}\n"
        return text

    def __add__(self, item):
        matrix = []
        if isinstance(item, (int, float)):
            for i, row in enumerate(self.matrix):
                matrix.append([])
                for elem in row:
                    matrix[i].append(elem + item)

        elif isinstance(item, Matrix):
            if self.size != item.size:
                raise ValueError("Matrices with different sizes.")

            for i, _ in enumerate(self.matrix):
                matrix.append([])
                for j, _ in enumerate(self.matrix[0]):
                    matrix[i].append(self.matrix[i][j] + item[i, j])

        return Matrix(matrix)

    def __mul__(self, item):
        matrix = []
        if isinstance(item, (int, float)):
            for i, row in enumerate(self.matrix):
                matrix.append([])
                for elem in row:
                    matrix[i].append(elem * item)

    def __sub__(self, item):
        matrix = []
        if isinstance(item, (int, float)):
            for i, row in enumerate(self.matrix):
                matrix.append([])
                for elem in row:
                    matrix[i].append(elem - item)

        elif isinstance(item, Matrix):
            if self.size != item.size:
                raise ValueError("Matrices with different sizes.")

            for i, _ in enumerate(self.matrix):
                matrix.append([])
                for j, _ in enumerate(self.matrix[0]):
                    matrix[i].append(self.matrix[i][j] - item[i, j])

        return Matrix(matrix)

    def __iter__(self):
        return iter(self.matrix)

    def _calc_determinant(self, matrix) -> float:
        """
        Funcao que calcula o determinante de uma matriz identidade de ordem n.
        Retorna um numero.
        """
        if len(matrix) != len(matrix[0]):
            return None
        if len(matrix) == 1:
            return matrix[0][0]

        det = 0
        for j, _ in enumerate(matrix[0]):
            new_matrix = [
                matrix[i + 1][:j] + matrix[i + 1][j + 1 :]
                for i, _ in enumerate(matrix[1:])
            ]
            if j % 2 == 0:
                det += matrix[0][j] * self._calc_determinant(new_matrix)
            else:
                det -= matrix[0][j] * self._calc_determinant(new_matrix)

        return det


def create_matrix() -> Matrix:
    """
    Funcao que cria uma matriz.
    Retorna uma matriz.
    """
    matrix = []
    while True:
        row = input(" > ")
        if not row:
            break
        row = [float(x) for x in row.split()]
        if matrix:
            if len(row) < len(matrix[0]):
                row += [0] * (len(matrix[0]) - len(row))
            elif len(row) > len(matrix[0]):
                for i, _ in enumerate(matrix):
                    matrix[i] += [0] * (len(row) - len(matrix[i]))
        matrix.append(row)

    return Matrix(matrix)
