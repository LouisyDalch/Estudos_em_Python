'''
4- Faça um programa que leia a idade, a altura e o peso de 30 pessoas, calcule e mostre:
a) a quantidade de pessoas com idade superior a 50 anos;
b) a média das alturas das pessoas com idade entre 10 e 20 anos;
c) a porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.
'''
quant=30

sup50=0

soma_h=0
idade10_20=0

menor40kg=0
for _ in range(quant+1):
    idade=int(input("Digite idade: "))
    altura=float(input("Digite altura: "))
    peso= float(input("Digite peso: "))

    if idade>50:
        sup50+=1
    if idade>10 and idade<20:
        soma_h+=altura
        idade10_20+=1
    if peso<40:
        menor40kg+=1

a = sup50
b = soma_h/idade10_20
c = (menor40kg/quant)*100

print("Quantidade de pessoas maiores de 50: ",a)
print(f"Média da altura de pessoas com idade entre 10 e 20 anos: {b:.2f}")
print(f"Pessoas de peso menor de 40 kg: {c:.2f}%")
    
    
