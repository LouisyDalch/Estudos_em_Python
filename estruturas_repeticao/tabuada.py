'''
Crie um programa em Python que solicite ao usuário um número inteiro (entre 0 e 9)
e exiba a tabuada desse número de 1 a 10. Utilize um loop for para imprimir o
resultado no formato:
'''
num = 0
while True:
    num=int(input("Digite um número inteiro de 0 a 9: "))
    if num>=0 and num<=9:
        break
    else:
        print("Número fora do intervalo!")
        continue
for i in range(1,11):
    print(num," x ",i," = ", num*i)
