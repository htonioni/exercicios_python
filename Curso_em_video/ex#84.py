pessoas = list()
secundaria = list()

lista_pesos = list()

menos_pesadas = list()
mais_pesadas = list()

# totp = 0 -> substituido pel len()

while True:
    secundaria.append(str(input('Digite seu nome: ')))
    secundaria.append(float(input('Digite seu peso em kg: ')))
    # Criada uma lista de pesos, posteriormente utilzamos max() e min()
    lista_pesos.append(secundaria[1])
    pessoas.append(secundaria[:])
    secundaria.clear()
    continuar = str(input('Gostaria de continuar? [S/N]: '))
    if continuar in ('Nn'):
        break

# Quais as pessoas com menor peso e mair peso
for c in pessoas:
    if max(lista_pesos) == c[1]:
        mais_pesadas.append(c[0])
    elif min(lista_pesos) == c[1]:
        menos_pesadas.append(c[0])

print('-=' * 45)
print(f'Voce cadastrou {len(pessoas)} pessoas!')
print(f'O maior peso foi {max(lista_pesos)}Kg. Peso de: {mais_pesadas}')
print(f'O menor peso foi {min(lista_pesos)}Kg. Pesos de: {menos_pesadas}')