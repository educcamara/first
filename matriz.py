"""
    Arquivo Python com funcoes para manipulacao de matrizes.
"""


class Matrix:
    """
    Classe Matrix
    """

    from typing import Tuple

    def __init__(self, matrix: [[float]]):
        self.matrix = matrix
        self.size = (len(matrix), len(matrix[0]))
        self.row = self.size[0]
        self.col = self.size[1]
        self.determinant = (
            self._calc_determinant(self.matrix)
            if self.size[0] == self.size[1]
            else "Non-square matrix."
        )

    # Recebe Elemento
    def __getitem__(self, coords: Tuple[int, int]):
        if isinstance(coords[0], int) and isinstance(coords[1], int):
            i = coords[0]
            j = coords[1]
            try:
                return self.matrix[i][j]
            except IndexError:
                return "Unreachable coordinates."

        if isinstance(coords[0], int):
            slc_i = slice(coords[0], coords[0] + 1, 1)
            slc_j = coords[1]

        elif isinstance(coords[1], int):
            slc_i = coords[0]
            slc_j = slice(coords[1], coords[1] + 1, 1)

        else:
            slc_i = coords[0]
            slc_j = coords[1]

        start_i, stop_i, step_i = slc_i.indices(self.row)
        start_j, stop_j, step_j = slc_j.indices(self.col)

        list_i = [x for x in range(start_i, stop_i, step_i)]
        list_j = [y for y in range(start_j, stop_j, step_j)]

        matrix = []
        for i, m in zip(list_i, [x for x, _ in enumerate(list_i)]):
            # print(f"m: {m}")
            matrix.append([])
            for j in list_j:
                # print(f"{j}", end=" ")
                matrix[m].append(self.matrix[i][j])
            # print()

        return Matrix(matrix)

    # Muda Elemento
    def __setitem__(self, coords: Tuple[int, int], value):
        i = coords[0]
        j = coords[1]
        try:
            self.matrix[i][j] = float(value)
            self.determinant = (
                self._calc_determinant(self.matrix)
                if self.size[0] == self.size[1]
                else "Non-square matrix."
            )
        except IndexError:
            pass

    # Representação em String
    def __repr__(self) -> str:
        text = ""
        for row in self.matrix:
            text += f"{row}\n"
        return text

    # Soma com Matriz
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
                    matrix[i].append(self.matrix[i][j] + item.matrix[i][j])
        else:
            raise TypeError("Invalid type.")

        return Matrix(matrix)

    # Subtração com Matriz
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
                    matrix[i].append(self.matrix[i][j] - item.matrix[i][j])
        else:
            raise TypeError("Invalid type.")

        return Matrix(matrix)

    # Multiplicação com Matriz
    def __mul__(self, item):
        matrix = []
        if isinstance(item, (int, float)):
            for i, row in enumerate(self.matrix):
                matrix.append([])
                for elem in row:
                    matrix[i].append(elem * item)

        elif isinstance(item, Matrix):
            for i, row in enumerate(self.matrix):
                matrix.append([])
                for k, _ in enumerate(item.matrix[0]):
                    result = 0
                    for j, val in enumerate(item):
                        result += row[j] * val[k]
                        # print(f'a{i+1}{j+1} b{j+1}{k+1}')
                    matrix[i].append(result)

        else:
            raise TypeError("Invalid type.")

        return Matrix(matrix)

    def __iter__(self):
        return iter(self.matrix)

    # Cálculo do determinante
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

    # Transposta da Matriz
    @property
    def transpose(self):
        """
        Propriedade que retorna a transposta de uma matriz.
        Retorna uma matriz.
        """
        t_matrix = []
        for j, _ in enumerate(self.matrix[0]):
            t_matrix.append([])
            for i, _ in enumerate(self.matrix):
                t_matrix[j].append(self.matrix[i][j])

        return Matrix(t_matrix)

    # Elemento Cofator
    def cofactor(self, i: int, j: int):
        """
        Função que calcula o cofator de um elemento.
        Retorna um número.
        """
        if i > self.size[0] or j > self.size[1]:
            return "Unreachable coordinates."

        minor = self._calc_minor(i, j)
        # print(f"Minor[{i}, {j}]: \n{minor}")
        factor = 1 if (i + j) % 2 == 0 else -1
        cof = minor.determinant * factor
        # print(f"Cofactor: {cof}")

        return cof

    def _calc_minor(self, i: int, j: int):
        """
        Função privada que retorna a matriz inferior ao elemento cofator.
        Retorna uma matriz.
        """
        minor = []
        for m, row in enumerate(self.matrix):
            if m != i:
                # quando o index m é diferente das coordenadas do elemento cofator:
                minor.append([elem for n, elem in enumerate(row) if n != j])
                # adicione à matriz inferior a linha de elementos exceto
                # o elemento cujo index é igual ao do elemento cofator

        return Matrix(minor)

    @property
    def adjugate(self):
        """
        Propriedade que retorna a matriz Adjunta.
        Retorna uma matriz.
        """
        cofactor_matrix = []
        for i, row in enumerate(self.matrix):
            cofactor_row = [self.cofactor(i, j) for j, _ in enumerate(row)]
            # print(cofactor_row)
            cofactor_matrix.append(cofactor_row)

        return Matrix(cofactor_matrix).transpose

    @property
    def inverse(self):
        """
        Propriedade que retorna a inversa de uma matriz.
        Retorna uma matriz.
        """
        if not self.determinant:
            return "This Matrix doesn't have inverse."
        return self.adjugate * (1 / self.determinant)


def c_matrix() -> Matrix:
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


def id_matrix(n: int) -> Matrix:
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

    return Matrix(matrix)


m1 = Matrix([[1, 2], [3, 4]])
m3 = Matrix([[1, 2, 2], [2, 3, 3], [3, 4, 4]])
m4 = Matrix([[1,2,3,4], [1,1,1,1], [3,4,4,5], [6,7,8,9]])
mi = id_matrix(2)
