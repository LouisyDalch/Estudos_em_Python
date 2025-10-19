'''
4 - Faça um programa que leia a idade, a altura e o peso de N pessoas, calcule e mostre:
a) a quantidade de pessoas com idade superior a 50 anos;
b) a média das alturas das pessoas com idade entre 10 e 20 anos;
c) a porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.
OBS: o usuário informa se quer continuar a execução ou não
'''
idade =0
altura=0.0
peso=0.0

qtd_50=0

soma_alt=0
qtd_10a20=0

qtd_pessoas=0
qtd_peso_40=0

while True:
    idade=int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))
    qtd_pessoas += 1

    if idade >50:
        qtd_50 += 1

    if idade>10 and idade<20:
        soma_alt += altura
        qtd_10a20 += 1
        
    if peso<40:
        qtd_peso_40 += 1

    opc = input("Deseja continuar?s/n ").lower()
    if opc=="s":
        continue
    elif opc == "n":
        break
    else:
        print("instrução não reconhecida!")

a = qtd_50
b = soma_alt/qtd_10a20
c = (qtd_peso_40/qtd_pessoas)*100

print(f"Quantidade de pessoas com mais de 50 anos: {a}")
print(f"Média das alturas das pessoas com idade entre 10 e 20 anos: {b:.2f}")
print(f"Percentual de pessoas com menos de 40 quilos: {c:.2f}%")
