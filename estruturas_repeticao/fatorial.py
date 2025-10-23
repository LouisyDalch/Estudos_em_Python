
def valida_num():
    n = int(input("Digite um número inteiro e positivo: "))
    while n<0:
        n = int(input("Digite um número inteiro e positivo: "))
    return n
n = valida_num()
fat = 1
if n!=0:
    for i in range(1,n+1):
        fat*=i    

print(n,"! = ",fat)
