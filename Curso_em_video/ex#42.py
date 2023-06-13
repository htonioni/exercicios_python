s1 = float(input('Digite um segmento: '))
s2 = float(input('Digite o segundo seguimento: '))
s3 = float(input('Digite o terceiro: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Forma um triângulo!')
    # if s1 == s2 == s3:
    if s1 == s2 and s2 == s3:
        print('E ele é \033[36mEQUILÁTERO\033[m')
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print('E ele é \033[36mISÓSCELES\033[m')
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print('E é um \033[36mESCALENO\033[m')
else:
    print('Não forma um triângulo!')
