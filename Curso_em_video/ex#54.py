from datetime import date

maiorID = 0
menorID = 0
hoje = date.today().year

for anos in range(1, 7 + 1):
    nasc = int(input('Qual o ano de nascimento da {}ª pessoa?: '.format(anos)))
    idade = hoje - nasc
    if idade >= 18:
        maiorID += 1
    else:
        menorID += 1
print(f'A quantidade de menores de idade é: {menorID}\n'
        f'E a quantidade de maiores de idade é: {maiorID}')
    

