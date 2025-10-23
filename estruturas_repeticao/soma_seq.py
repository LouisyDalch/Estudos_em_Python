'''
Escreva um programa em Python que solicite um número inteiro positivo N ao usuário
e calcule a soma de todos os números inteiros de 1 a N. Utilize um loop for para
realizar a soma e exiba o resultado.
'''

def verifica_numero():
    n = int(input("Digite um número inteiro positivo! "))
    while n<=0:
        n = int(input("Digite um número inteiro positivo! "))
    return n
n = verifica_numero()
soma = 0
for i in range(1,n+1):
    soma+=i
print("soma de 1 até ",n, " = ",soma)
