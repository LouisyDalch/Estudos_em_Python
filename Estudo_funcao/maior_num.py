def maior_num(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

print(maior_num(a,b,c))
        
