from time import sleep

peso = float(input('Qual seu peso?: '))
altura = float(input('E qual sua altura?: '))
imc = peso / (altura ** 2)
print(f'Ok seu \033[31mIMC\033[m é de {imc:.2f}!')
sleep(0.8)
if imc < 18.5:
    print(f'Seu IMC de {imc:.2f} está para pessoas abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Esse é seu índice ideal!')
elif 25 <= imc < 30:
    print('Você está acima do peso!')
elif 30 <= imc < 40:
    print('Você está bastante acima do peso!')
elif imc > 40:
    print('Procure um profissional da área media, agora!')
