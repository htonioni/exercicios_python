# Separar os 7 valores do usuario em duas listas, uma par e uma impar

lista = [[],[]]


for valnum in range(1,8):
    x = int(input(f"Digite o {valnum}º valor: "))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)

lista[0].sort()
lista[1].sort()
print(f"Os valores impares foram: {lista[0]}")
print(f"Os valores pares foram: {lista[1]}")