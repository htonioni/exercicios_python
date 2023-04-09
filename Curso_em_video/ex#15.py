km = int(input('Bem vindo a Localiza, quantos KM voce percorreu?: '))
days = int(input('Quantos dias você utilizou o carro?: '))
k2 = km * 0.15
d2 = days * 60
print(f'Você andou {days} dias com o carro, o que resulta em R${d2} e pela gasolina R${k2}.'
      f'Logo seu total é de R${k2+d2}')