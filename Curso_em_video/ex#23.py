num = int(input('Digita um número interiro ai de 0 até 9999: '))
und = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print(f'Anlise do numero: {num}\n'
        f'A unidade deste número é: {und}\n'
        f'A dezena deste número é: {dez}\n'
        f'A centena deste número é: {cent}\n'
        f'A milhar deste número é: {mil}\n')