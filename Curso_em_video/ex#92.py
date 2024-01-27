from datetime import date

dicio = dict()
current_year = date.today().year

dicio["Nome"] = str(input("Digite seu nome: "))
user_birth = int(input("Digite seu ano de nascimento: "))
dicio["Idade"] = current_year - user_birth
dicio["ctps"] = int(input("Digite sua carteira de trabalho [0 -> nulo]: "))
if dicio["ctps"] != 0:
    dicio["Admissão"] = int(input("Qual seu ano de admissão: "))
    dicio["Salario"] = float(input("Qual seu salário: "))
    ano_aposent = dicio["Admissão"] + 35
    dicio["Aposentadoria"] = ano_aposent - user_birth
print("-=-" * 20)
for k, v in dicio.items():
    print(f"{k} tem o valor {v}")