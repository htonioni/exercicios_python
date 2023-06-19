from random import choice
from time import sleep

print('OK! VAMOS PARA O JOKEN PO\n'
        '\033[31mSuas opções são:\033[m\n'
        '[ 1 ] \033[35mPEDRA\033[m\n'
        '[ 2 ] \033[36mPAPEL\033[m\n'
        '[ 3 ] \033[33mTESOURA\033[m')
esc = int(input('Qual sua escolha?: '))
esc_c = choice([1, 2, 3])
if esc == esc_c:
    print('Puts, o computador escolheu o mesmo que você!')
elif esc_c == 1:
    print('O computador escolheu \033[35mPEDRA\033[m')
    if esc == 2:
        print('Você escolheu \033[36mPAPEL\033[m, logo você\n'
                '     \033[31mGANHOU!!!!!!\033[m')
    elif esc == 3:
        print('PEDRA ganha de tesoura, logo você\n'
                '   \033[31mPERDEUUUUUU!!!!!!\033[m')
elif esc_c == 2:
    print('O computador escolheu \033[36mPAPEL\033[m')
    if esc == 1:
        print('Você escolheu \033[35mPEDRA\033[m\n'
                'PEDRA perde de papel, logo você:\n'
                '    \033[31mPERDEUUUUUU!!!!!!\033[m')
    elif esc == 3:
        print('Você escolheu \033[33mTESOURA\033[m\n'
                'TESOURA ganha de PAPEL logo você\n'
                '\033[31mGANHOU!!!!!!\033[m')
elif esc_c == 3:
    print('O computer escolheu TESOURA...')
    sleep(.5)
    print(f'Você escolheu {esc}')
    if esc == 1:
        print('Você escolheu \033[35mPEDRA\033[m\n'
                'PEDRA vence de TESOURA, logo você\n'
                '\033[31mGANHOU!!!!!!\033[m')
    elif esc == 2:
        print('Você escolheu \033[36mPAPEL\033[m\n'
                'TESOURA vence de PAPEL, logo você\n'
                '\033[31mPERDEUUUUUU!!!!!!\033[m')
