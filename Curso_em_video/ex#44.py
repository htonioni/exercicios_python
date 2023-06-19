print(f'{" Mercado da esquina :) ":=^40}')
preco = float(input('Qual o \033[32mpreço\033[m total das suas compras?: '))
print('''Qual seria a forma de \033[31mpagamento\033[m?
[ 1 ] à vista dinheiro/cheque (\033[34m10% de desconto\033[m)
[ 2 ] à vista cartão (\033[36m5% de desconto\033[m)
[ 3 ] 2x no cartão (\033[35mSem juros\033[m)
[ 4 ] 3x ou mais no cartão (\033[33mjuros de 20%\033[m)''')
esc = int(input(': '))
if esc == 1:
    stats = f'R${preco - (preco * 0.1)} aplicando o desconto de 10%'
elif esc == 2:
    stats = f'R${preco - (preco * 0.05)} aplicando o desconto de 5%'
elif esc == 3:
    stats = f'duas parcelas de R${preco / 2} sem juros'
elif esc == 4:
    parcelas = int(
        input('Quantas parcelas serão?: '))
    stats = f'em {parcelas} parcelas de {((preco * 0.2) + preco) / parcelas}'
else:
    stats = preco
    print('\033[31mERRO!!!!!\033[m')
print(f'O seu total de R${preco} ficara {stats}')
