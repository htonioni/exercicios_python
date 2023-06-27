input('Aperte \033[31menter\033[m para descobrir a soma de todos os números \033[31mÍMPARES\033[m '
        'multiplos de 3 entre 1 e 500!')
soma = 0
count = 0
for c in range(0, 500, 3):
    if c % 2 != 0:
        count = count + 1
        soma = soma + c
print(f'\033[36m{count}\033[m números foram somados, e o resultado dessa soma foi \033[36m{soma}\033[m')
