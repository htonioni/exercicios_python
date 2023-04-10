l_a = str(input('Digita uma frase ai, pode ser grande: ')).strip()
print(f'A quantidade de A na sua frase é de: {l_a.lower().count("a")}\n'
        f'Ela aparece a primeira vez em {l_a.lower().find("a"[0:]) + 1}\n'
        f'E ela aparece a ultima vez em {l_a.lower().rfind("a")}')