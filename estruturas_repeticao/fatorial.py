'''
2- Codifique um programa que calcule o fatorial de um número natural n informado pelo usuário.
'''
n=0
while True:
    n = int(input("Digite um número natural: "))
    if n<0:
        print("Esse número não é natural!")
        continue
    else:
        break
fat = 1
if n != 0:
    for i in range(1,n+1,1):
        fat*=i
print("fatorial = ",fat)
