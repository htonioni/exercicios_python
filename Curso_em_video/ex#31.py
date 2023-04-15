print('Vamos apara o exercicio viagem')
km = float(input('Qual a distancia \033[31mem km\033[m da sua viajem?: '))
if km <= 200:
    # print(f'A sua viagem de {km}km terá o preço de R${km*0.5:.2f}')
    preco = km * 0.5
else:
    # print(f'O preço da sua passagem é R${km*0.45:.2f}')
    preco = km * 0.45
print(f'A sua viagem de {km}km terá o valor de \033[31;4mR${preco:.2f}')

