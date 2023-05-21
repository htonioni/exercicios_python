num3_1 = int(input('Digite um número inteiro: '))
num3_2 = int(input('Digite outro número inteiro: '))
if num3_1 > num3_2:
    print('O\033[4m primeiro\033[m número é\033[31;1m maior\033[m')
elif num3_1 < num3_2:
    print('O \033[4msegundo\033[m número é \033[1;31mmaior\033[m')
elif num3_1 == num3_2:
    print('Os valores são', 'iguais'.upper())
