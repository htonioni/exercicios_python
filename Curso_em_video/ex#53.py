frase_cru = str(input('Digite a frase para analise: '))
frase_tratada = frase_cru.upper().replace(' ', '')
tamanho = len(frase_tratada)
frase_contraria = ''

for contrario in range(tamanho - 1, -1, -1):
    frase_contraria = frase_contraria + frase_tratada[contrario]
if frase_contraria == frase_tratada:
    print(f'Está frase \033[31mé um polndromo!\033[m \n'
            f'Frase: {frase_tratada}\n'
            f'Ao contrario: {frase_contraria}')
else:
    print(f'A frase {frase_tratada} não é igual a {frase_contraria}')



