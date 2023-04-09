nomec = input(str('Qual seu nome completo?\n'))
print(f'O seu nome com todas maiúsculas será:\n{nomec.upper()}\n'
        f'O seu nome com todas minúsculas será:\n{nomec.lower()}\n'
        f'O seu nome possui {len(nomec.strip()) - nomec.count(" ")} caracteres\n'
        f'E o primeiro nome possui {len(nomec.split()[0])} caracteres')