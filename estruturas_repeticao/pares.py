def valida_num():
    n = int(input("Digite um número inteiro positivo: "))
    while n<=0:
        n = int(input("Digite um número inteiro positivo: "))
    return n
n = valida_num()
for i in range(2,n+1,2):
    print(i)
