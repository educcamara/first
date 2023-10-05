"""
    Arquivo Python com funcoes para manipulacao de matrizes.
"""

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
    print("Digite a primeira matriz em forma de lista de listas:")
    matrix1 = eval(input(" > "))
    print("Digite a segunda matriz em forma de lista de listas:")
    matrix2 = eval(input(" > "))

    print(multiply_matrix(matrix1, matrix2))
    return 0


main()
