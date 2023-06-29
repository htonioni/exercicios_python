soma = 0
c = 0
for sum_number in range(1, 6 + 1):
    number = int(input(f'Digite o {sum_number} número: '))
    if number % 2 == 0:
        c += 1
        soma += number
print(f'Achei {c} números pares, e a soma é \033[31m{soma}\033[m')
