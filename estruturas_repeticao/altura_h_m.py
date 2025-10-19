'''
- Escreva um programa em Python que leia o gênero e a altura de N pessoas, calcule e mostre a altura
média
das mulheres e dos homens separadamente. Utilize o comando de repetição que desejar
'''

genero =""
altura =0.0
soma_M =0
soma_H =0
cont_h =0
cont_m =0
while True:
    altura = float(input("Digite a altura! "))

    if altura <= 0:
        break
    else:
        genero = input("Homem ou mulher?(h/m) ").lower()

        if genero == "h":
            soma_H += altura
            cont_h += 1
        elif genero == "m":
            soma_M += altura
            cont_m += 1

media_h = soma_H/cont_h
media_m = soma_M/cont_m

print(media_h,media_m)
