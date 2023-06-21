from datetime import date
from time import sleep

fim_d_ano = 12 - date.today().month
print(f'Ok, faltam \033[31m{fim_d_ano} meses\033[m para o fim do ano, mas la vai....')
sleep(.5)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[31mFELIZ ANO NOVO!\033[m')