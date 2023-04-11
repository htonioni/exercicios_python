# Faça um programa que ajude um jogador do MEGA SENA a criar palpite=. O programa vai perguntar quantos jogos serño gerados a vai sortear 6 números entro 1 e 60 para cada jogo, cadastrando tudo em uma lista composto.

from time import sleep
from random import randint, choice

print("-="*25)
print("Jogo da Mega Sena".center(50))
print("-="*25)

user_input = int(input("Quantos jogos voce quer que eu sorteie?: ")) 

lista = list()
lista_todos_jogos = list()

tot_jogos = 0
print("-=" * 3, f"Sorteando os {user_input} JOGOS", "-="* 3)
while tot_jogos <= user_input-1:
    counter = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            counter += 1
        if counter >= 6:
            break
    lista.sort()
    lista_todos_jogos.append(lista[:])
    lista.clear()
    print(f"O jogo numero {tot_jogos+1} foi: ",lista_todos_jogos[tot_jogos])
    sleep(.8)
    tot_jogos += 1
# print(f"Os numeros sorteados foram: {lista_todos_jogos}")
