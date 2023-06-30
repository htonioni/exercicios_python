vezes_dividido = 0
continuar = True

while continuar:
    num1 = int(input('\n*Digite \033[32m0\033[m para sair*\n'
                        'Digite um número inteiro: '))
    if num1 == 0:
        break
    for primo in range(1, num1 + 1):
        div = num1 % primo
        if div == 0:
            vezes_dividido += 1

            print(f'\033[31m{primo}\033[m', end=' ')
            continue
        print(primo, end=' ')
    print(f'\nO número \033[31m{num1}\033[m foi divisível '
            f'\033[36m{vezes_dividido} vezes\033[m, por isso ele: ')

    if vezes_dividido == 2:
        print('\033[31mÉ\033[m um número primo!')

    elif vezes_dividido >= 3:
        print('\033[31mNÃO\033[m é um primo!')

