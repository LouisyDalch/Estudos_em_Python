#contadores:
dc = 0
gb = 0
pm = 0
ra = 0
tc = 0
vn = 0
vb = 0

while True:
    print("|==== URNA ELEITORAL ====|")
    print("1 – DACENA")
    print("2 - GUILHERME BOLHAS")
    print("3 – PABLO MARCADO")
    print("4 - RICARDO ANTIGO")
    print("5 – TABATA CHATRAL")
    print("6 - VOTAR NULO")
    print("7 - VOTAR EM BRANCO")
    print("0 - FINALIZAR VOTAÇÃO")
    
    voto = int(input("Digite para votar: "))
    match voto:
        case 1:
            dc +=1
        case 2:
            gb +=1
        case 3:
            pm += 1
        case 4:
            ra += 1
        case 5:
            tc += 1
        case 6:
            vn += 1
        case 7:
            vb+= 1
        case 0:
            print("VOTAÇÃO ENCERRADA!!!")
            break
        case _:
            print("Voto inválido!")

print("DACENA = ", dc)
print("GUILHERME BOLHAS = ", gb)
print("PABLO MARCADO = ", pm)
print("RICARDO ANTIGO = ", ra)
print("TABATA CHATRAL = ", tc)
print("NULO = ", vn)
print("BRANCO = ", vb)
