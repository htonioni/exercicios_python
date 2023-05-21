num2 = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
#        print('Escolha uma base para converter:\n'
#              '[ 1 ] converter para BINÁRIO\n'
#              '[ 2 ] converter para OCTAL\n'
#              '[ 3 ] converter para HEXADECIMAL')
base = int(input('Sua escolha: '))
if base == 1:
    print(
        f'O número {num2} convertido para binário é: {bin(num2)[2:]}')
elif base == 2:
    print(
        f'O número {num2} convertido para OCTAL é: {oct(num2)[2:]}')
elif base == 3:
    print(
        f'Seu numero {num2} convertido para HEXADECIMAL é: {hex(num2)[:2]}')
else:
    print('Valor incorreto!')
