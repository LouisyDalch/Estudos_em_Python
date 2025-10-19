aux=""
num=0
while True:
    num = int(input("Digite um número: "))
    if num>0:
        aux = "Positivo"
    elif num<0:
        aux = "Negativo"
    else:
        break
    print(aux,num)
