# dicio = {"Nome":"", "Media":0, "Situação":""}
dicio = dict()
user_name = str(input("Nome: "))
user_grade = float(input("Media: "))
dicio["Nome"] = user_name
dicio["Média"] = user_grade
if dicio["Média"] >= 7:
    dicio["Situação"] = "Aprovado"
elif dicio["Média"] >= 4:
    dicio["Situação"] = "Recuperação"
else:
    dicio["Situação"] = "Reprovado"

for k, v in dicio.items():
    print(f"{k} eh igual a {v}")
