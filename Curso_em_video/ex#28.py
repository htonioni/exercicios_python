from random import choice
from time import sleep

print('\033[1;32mOk vamos lá então\033[m')
#   alea = radint(0, 5)
alea = choice([0, 1, 2, 3, 4, 5])
print('Estarei pensando aqui em um numero ..........')
sleep(2.0)
numale = int(input('Ok, digita um número de \033[31m0\033[m à \033[31m5\033[m: '))
if numale == alea:
    print('True')
else:
    print(f'Eu ganhei! Pensei no número {alea} e não em {numale}')
    quit(f'Mais sorte na proxima!')

