print('Vamos lá ta na hora de calcular seu aumento')
salario = float(input('Qual seu salário? '))
if salario > 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.5
print(f'Seu novo salario será de {aumento}')
