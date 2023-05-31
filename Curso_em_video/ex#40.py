nota_1 = float(input('Qual foi a sua nota na primeira prova?: '))
nota_2 = float(input('E qual a nota na segunda prova?: '))
media = (nota_1 + nota_2) / 2
if media >= 7:
    print(f'Parabéns pelas notas, a media foi {media} e está \033[31;4mAPROVADO!\033[m')
elif media < 5:
    print(f'Que pena, media de {media} você \033[31mREPROVOU\033[m')
elif 7 > media >= 5:
    print(f'Bom, com uma média de {media} você ficou de \033[31mRECUPERAÇÃO\033[m')


