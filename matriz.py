"""
    Arquivo Python com funções para manipulação de matrizes.
"""

print("Digite a primeira matriz em forma de lista de listas:")
m1 = eval(input(" > "))
print("Digite a segunda matriz em forma de lista de listas:")
m2 = eval(input(" > "))

matriz3 = []

for i, row in enumerate(m1):
    matriz3.append([])
    for k, col in enumerate(m2[0]):
        result = 0
        for j, val in enumerate(m2):
            result += row[j] * val[k]
            # print(f'a{i+1}{j+1} b{j+1}{k+1}')
        matriz3[i].append(result)

print("A multiplicação das duas matrizes resultou em:")
print(matriz3)

# exemplo: [[1,2],[2,1]] [[1,0],[0,1]]
