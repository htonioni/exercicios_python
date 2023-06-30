peso = []

for kg in range(1, 5 + 1):
    pessoa = float(input(f'Qual o peso da {kg}ª pessoa?: '))
    peso.append(pessoa)

print(f"\nA pessoa de maior peso foi a pessoa com {max(peso)} KG's\n"
        f"A pessoa com menor peso foi a pessoa com {min(peso)} KG'S")
