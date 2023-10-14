from matriz import Matrix


def get_str_coords(text: str) -> tuple:
    text.replace('(', '')
    text.replace(')', '')
    text.replace(' ', '')
    x, y, z = text.split(',')

    return int(x), int(y), int(z)


input_1 = input("Digite as coordenadas do ponto 1: ")
input_2 = input("Digite as coordenadas do ponto 2: ")
input_3 = input("Digite as coordenadas do ponto 3: ")

ponto_1 = get_str_coords(input_1)
ponto_2 = get_str_coords(input_2)
ponto_3 = get_str_coords(input_3)

vetor_1 = [ponto_1[0] - ponto_2[0], ponto_1[1] - ponto_2[1], ponto_1[2] - ponto_2[2]]
vetor_2 = [ponto_3[0] - ponto_2[0], ponto_3[1] - ponto_2[1], ponto_3[2] - ponto_2[2]]

matriz = Matrix([[1, 1, 1], vetor_1, vetor_2])
c1 = matriz.cofactor(0, 0)
c2 = matriz.cofactor(0, 1)
c3 = matriz.cofactor(0, 2)

area = (c1**2 + c2**2 + c3**2)**(1/2)/2

print(round(area, 3))

# print(ponto_1, ponto_2, ponto_3)

# Digite as coordenadas do ponto 1: -1, -1, -1
# Digite as coordenadas do ponto 2: 1, 1, 1
# Digite as coordenadas do ponto 3: 2, 3, 4
