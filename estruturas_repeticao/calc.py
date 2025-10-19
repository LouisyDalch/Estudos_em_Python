opc=0

def operacoes(opc,n1,n2):
    res = 0
    match opc:
        case 1:
            res = n1+n2
        case 2:
            res = n1-n2
        case 3:
            res = n1*n2
        case 4:
            res = n1/n2
        case _:
            res = "resultado inváido"
    return res
            
while True:
    print("|==== MENU DE OPÇÕES ====|")
    print("Digete...")
    print("1-Somar")
    print("2-Subtrair")
    print("3-Multiplicar")
    print("4-Dividir")
    print("5-Sair")
    opc = int(input("Opção desejada: "))
    
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    
    if opc !=5:
        print(operacoes(opc,n1,n2))
    else:
        break
    
    
