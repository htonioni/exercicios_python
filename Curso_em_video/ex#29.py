print('-_-' * 20)
print('\033[4mVoce foi pego na blitz.......... ')
print('-_-' * 20)
vel = float(input('Agora fala ai qual \033[31mkm/h\033[m vc estava?: '))
if vel > 80:
    print(f'Voce sera multado em \033[4;31mR${(vel - 80) * 7:.2f}')
else:
    print('Esta liberado ')

