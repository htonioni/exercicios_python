people_list = list()
person_dict = dict()
person_counter = 0

while True:
    person_dict["Name"] = str(input("Nome: "))
    person_dict["Sex"] = str(input("Sexo [M/F]: "))
    while person_dict["Sex"] not in ("MFmf"):
        print("\033[31mERRO! Por favor digite apenas M ou F\033[m")
        person_dict["Sex"] = str(input("Sexo [M/F]: "))

    person_dict["Age"] = int(input("Idade: "))

    people_list.append(person_dict.copy())

    user_choice = str(input("Quer continuar [S/N]: "))
    while user_choice not in ("SNsn"):
        print("\033[31m ERRO! Responda apenas S ou N.\033[m")
        user_choice = str(input("Quer continuar [S/N]: "))
    
    person_counter +=1
    if user_choice.upper() == "N":
        break

age_total = 0
female_person = list()
for each_people in people_list:
    age_total += each_people["Age"]
    if each_people["Sex"] in ("Ff"):
        female_person.append(each_people["Name"])
media = age_total / person_counter

print("-="*30)
print(f"A) Ao todo temos {person_counter} pessoas cadastradas")
print(f"B) A media de idade é de {media:.2f}")
print(f"C) As mulheres cadastradas foram: {female_person}")
print(f"D) A lista das pessoas que estão acima da média:")
for person in people_list:
    if person["Age"] > media:
        print(f"    Nome = {person['Name']}; Sexo = {person['Sex']}; Idade = {person['Age']}")
print("ENCERRADO".center(20, "-"))
