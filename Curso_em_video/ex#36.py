from time import sleep
print('Bem vindo ao banco, você gostaria de um empréstimo, certo? .....')
sleep(0.8)
salario = float(input('Qual seu salário?: '))
anos = int(input('Deseja pagar em quantos anos?: '))
meses = anos * 12
casa = float(input('Qual o valor da casa?: '))
if casa >= 1000000:
    print('EITA! Que casa cara.')
trinta = salario * 0.3
prest = casa / meses
if prest > trinta:
    print('Infelizmente não conseguiremos conceder um empréstimo!')
elif prest <= trinta:
    print(f'Esta ok, a prestação fica \033[31mR${prest:.2f}\033[m'
            'por mês no período de'
            f'\033[31m{anos}\033[m anos')
    sleep(0.8)
    print('Agradecemos a preferência, volte sempre!')