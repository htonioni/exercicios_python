from datetime import date

ano = int(input('Qual seu ano de nascimento?: '))
idade = date.today().year - ano
if idade > 18:
    atrasado = (idade - 18) * 12
    print(
        f'Você ja passou do seu alistamento, esta {atrasado} meses \033[31;2matrasado!!!!!\033[m')
elif idade < 18:
    falta = (18 - idade) * 12
    print(f'Você ainda não pode se alistar, faltam {falta}' 
            'meses para realizar seu alistamento')
elif idade == 18:
    print('\033[31;1mEstá na hora de se alistar\033[m,'
            'corra para a junta militar no Aterrado')

