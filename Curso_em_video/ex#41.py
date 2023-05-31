from datetime import date

nasc = int(input('Qual seu ano de nascimento?: '))
idade = date.today().year - nasc
print(f'O atleta tem anos {idade}')
if idade <= 9:
    print('Sua classificação é \033[36;4mMIRIM\033[m')
elif 9 < idade <= 14:
    print('Sua classificação é \033[36;4mINFANTIL\033[m')
elif 14 < idade <= 19:
    print('Sua classificação é \033[36;4mJUNIOR\033[m')
elif 19 < idade <= 25:
    print('Sua classificação é \033[36;4mSÊNIOR\033[m')
else:
    print('Sua classificação é \033[36;4mMASTER\033[m, Parabéns!')

