def soma_para_triangulo(a,b,c):
    if(a+b > c):
        return 1
    else:
        return 0
def tipo_triangulo(a,b,c):
    if(a==b or a==c or c==b):
        return "Isósceles"
    elif(a==b and a==c):
        return "Equilátero"
    else:
        return "Escaleno"

print("Entre com os lados do triângulo! ")
a = float(input())
b = float(input())
c = float(input())

if(a>0 and b>0 and c>0):
    if(soma_para_triangulo(a,b,c) == 0):
        print("Não é triângulo!")
    else:
        print(tipo_triangulo(a,b,c))
else:
    print("Todos os lados de um triângulo devem ser maiores que 0!")
