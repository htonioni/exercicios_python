# cada jogador sera um dict
# no final teremos a lista do time

football_team = list()
# football_team = [{'Name': 'Hugo', 'Gols': [2, 2, 0, 2], 'Total': 6}, {'Name': 'Joao', 'Gols': [2, 0], 'Total': 2}, {'Name': 'Karlo', 'Gols': [2], 'Total': 2}]


while True:
    player = dict()
    gols = list()
    player["Name"] = str(input("Nome do jogador: "))
    total_played = int(input("Quantas partidas ele jogou?: "))
    counter = 1
    while counter <= total_played:
        gol = (int(input(f"    Quantos gols na partida {counter}?: ")))
        gols.append(gol)
        counter += 1

    player["Gols"] = gols[:]
    player["Total"] = sum(gols)
    football_team.append(player.copy())
    user_choice = str(input("Quer continuar? [S/N]: "))
    while user_choice.upper() not in ("SN"):
        print("ERRO! Utilize apenas S ou N")
        user_choice = str(input("Quer continuar? [S/N]: "))
    if user_choice.upper() == "N":
        break
print(football_team)
print("-="*35)
print(f"{'COD':<4}{'NOME':<20}{'GOLS':<20}{'TOTAL':<6}")
print("-"*50)
for i, val in enumerate(football_team):
    gol_str = str(val['Gols'])
    print(f"{i:>3}", f"{val['Name']:<19}", f"{gol_str:<19}", f"{val['Total']:<4}")
print("-"*50)
while True:
    user_input = int(input("Mostrar dados de qual jogador? [99 = quit]: "))
    if user_input == 99:
        break
    elif user_input > len(football_team):
        print(f"ERRO! Nao existe jogador {user_input}")
        continue
    print(f"-- LEVANTAMENTO DO JOGADOR {football_team[user_input]['Name']}")
    for indice in range(0,len(football_team[user_input]['Gols'])):
        print(f"No jogo {indice+1} ele fez {football_team[user_input]['Gols'][indice]} gols.")
    print("-"*50)

