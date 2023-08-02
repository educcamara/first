m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]] 

matriz3 = []

for i in range(len(m1)):
    matriz3.append([])
    for k in range(len(m2[0])):
        elem = 0
        for j in range(len(m2)):
            elem += (m1[i][j] * m2[j][k])
            print(f'a{i+1}{j+1} b{j+1}{k+1}')
        matriz3[i].append(elem)

print(matriz3)