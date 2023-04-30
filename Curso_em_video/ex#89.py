lista_completa = []
li_aux = []
counter = 0
while True:
    user_name = str(input("Nome: "))
    li_aux.append(user_name)
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    li_aux.append(n1)
    li_aux.append(n2)
    lista_completa.append(li_aux[:])
    li_aux.clear()
    choice = str(input("Gostaria de continuar? [S/N]:"))
    if choice.upper() in ("N"):
        break
print("-="*35)
print(f'{"No.":<6}{"NOME":<10}{"MÉDIA":>13}')
print("-"*30)
for pessoa in lista_completa:
    print(f"{counter:<6}{lista_completa[counter][0]:<10}", end="")
    print(f"{(lista_completa[counter][1]+lista_completa[counter][2])/2:>12.1f}")
    counter += 1
print("-"*40)
while True:
    grade = int(input("Mostras as notas de qual aluno?(999 interrompe): "))
    if grade == 999:
        break
    else:
        print(f"Notas de {lista_completa[grade][0]} são: {lista_completa[grade][1]} e {lista_completa[grade][2]}")
print("FINALIZANDO....")
print("<<< VOLTE SEMPRE >>>")
