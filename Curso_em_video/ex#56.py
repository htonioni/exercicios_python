c = 0
age = 0
mais_velho = 0
nome2 = ''
c_2F = 0

for data in range(1, 5):
    print(f'   \033[31m{data}ª\033[m PESSOA')

    nome = str(input('Qual seu nome?: '))

    age_input = int(input('Qual sua idade?: '))
    age = age_input + age
    c = c + 1

    sex = str(input('Qual seu sexo, [M ou F]?: '))
    if sex.lower() == 'm':
        if data == 1:
            mais_velho = age_input
            if nome2 == '':
                nome2 = nome
        elif mais_velho < age_input:
            mais_velho = age_input
            nome2 = nome
    else:
        if age_input < 20:
            c_2F += 1

med_idade = age / c

print(f'\nA média das idades é: \033[31m{med_idade:.1f} anos\033[m'
        f'\nO nome homem mais velho é: \033[31m{nome2.capitalize()}\033[m'
        f'\nA quantidade de mulheres com menos de 20 anos é: '
        f'\033[31m{c_2F} mulheres\033[m')