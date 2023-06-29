num = int(input('Digite um número inteiro para saber sua tabuada: '))
for tabuada in range(1, 10 + 1):
    print(f'{tabuada} x {num} = \033[31m{num * tabuada}\033[m')

print('\nObrigado, volte sempre!')
