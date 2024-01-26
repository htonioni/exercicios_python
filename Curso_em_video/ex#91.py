from random import randint
from time import sleep as pausa
from operator import itemgetter

dicionario = dict()
winner_count = 1


input("Aperte enter para começar!")
print("Valores sorteados: ")
for jog in range(1,4+1):
    if jog == 0:
        continue
    dicionario[f"Jogador{jog}"] = randint(1,6)

for k, v in dicionario.items():
    print(f"   O {k} tirou {v}")
    pausa(.7)

dict_ordenado = sorted(dicionario.items(), reverse=True, key=itemgetter(1))
print("Ranking do jogadores: ")
for counter,winner in enumerate(dict_ordenado):
    print(f"   {counter+1}° lugar: {winner[0]} com {winner[1]}")
    
