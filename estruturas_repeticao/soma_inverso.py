'''
1- Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma:
S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n
'''
n=0
while True:
    n = int(input("Digite um número inteiro e positivo! "))
    if n > 0:
        break
    else:
        print("Esse númedo é negativo ou nulo!")
        continue

s =1
for i in range(n+1):
    if i>1: #1/1=1, isso é, estava sendo somado duas vezes.
        s+=1/i
print(s)
