# Criacao de uma matriz [2 , 2]

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for lin in range(0,3):
        for col in range(0,3):
                matriz[lin][col] = int(input(f"Digite um numero para [{lin}, {col}]: "))
for lin in range(3):
        for col in range(3):
            print(f"[{matriz[lin][col]:^5}]", end=" ")
        print()
