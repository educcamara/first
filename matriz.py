"""
    Arquivo Python com funcoes para manipulacao de matrizes.
"""


def create_matrix() -> [[int]]:
    """
    Funcao que cria uma matriz.
    Retorna uma matriz.
    """
    matrix = []
    while True:
        row = input(" > ")
        if not row:
            break
        row = [int(x) for x in row.split()]
        if matrix:
            if len(row) < len(matrix[0]):
                row += [0] * (len(matrix[0]) - len(row))
            elif len(row) > len(matrix[0]):
                for i, _ in enumerate(matrix):
                    matrix[i] += [0] * (len(row) - len(matrix[i]))
        matrix.append(row)

    return matrix


def multiply_matrix(matrix1, matrix2):
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


def main():
    """
    Funcao principal.
    """

    return 0


main()
