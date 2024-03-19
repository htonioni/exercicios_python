counter = 0
dicio = dict()
lista = list()

dicio["Nome"] = str(input("Nome do Jogador: "))
game_total = int(input(f"Quantas partidas {dicio['Nome']} jogou?: "))

while counter != game_total:
    lista.append(int(input(f"    Quantos gols na partida {counter}?: ")))
    counter += 1
dicio["Gols"] = lista[:]
dicio["Total"] = sum(lista)

print("-="*30)
print(dicio)
print("-="*30)

for k, v in dicio.items():
    print(f"O campo {k} tem o valor {v}")

print("-="*30)
print(f"O jogador {dicio['Nome']} jogou {game_total} partidas.")
for cont, gol in enumerate(dicio["Gols"]):
    print(f"  => Na partida {cont}, fez {gol} gols.")
print(f"Foi um total de {dicio['Total']} gols")
