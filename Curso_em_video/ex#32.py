ano = int(input('Gostaria de verificar se um ano é bissexto? Digita ele ai: '))
div = ano % 4
print(div)
if div == 0 and div % 100 != 0 or div % 400 == 0:
    print(f'{ano} é um ano BISSEXTO')
else:
    print(f'{ano} não é um ano BISSEXTO')
