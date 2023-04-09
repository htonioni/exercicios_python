cid = str(input('Qual o nome da sua cidade?: ')).strip()
#   Sempre colocar o .strip no input, para ele ja cortar os espaços
#   Aqui embaixo nos pegamos a cidade e colocamos em maisculas, logo após checamos se há 'SANTO' maiusculo nela
if cid[0:5].upper() == 'SANTO':
    print(f'Há Santo no começo de {cid}')
else:
    print('Não há Santo no começo da sua cidade')