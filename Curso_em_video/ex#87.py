matriz = [[0,0,0],[0,0,0],[0,0,0]]
sum_par = sum_col = 0
for col in range(0,3):
    for lin in range(0,3):
        matriz[col][lin] = int(input(f"Digite um valor para [{col},  {lin}]: "))
        if lin == 2:
            sum_col += matriz[col][lin]
        if matriz[col][lin] % 2 == 0:
            sum_par += matriz[col][lin]
print("-="* 35)
for col in range(3):
    for lin in range(3):
        print(f'[{matriz[col][lin]:^5}]', end=" ")
    print()
print("-="* 35)
print(f"A soma dos valores pares eh: {sum_par}")
print(f"A soma dos valores da terceira coluna eh: {sum_col}")
print(f"O maior valor da segunda linha eh: {max(matriz[1])}")
