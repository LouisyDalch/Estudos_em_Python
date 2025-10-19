tipo = input("Digite o tipo: ").upper()
qtd_d = int(input("Digite a qtd dias: "))

if (tipo == 'S'):
    total = qtd_d*255.5
    print(f"TOTAL = {total}")
elif (tipo == 'D'):
    total = qtd_d*305.5
    print(f"TOTAL = {total}")
elif (tipo == 'T'):
    total = qtd_d*360.5
    print(f"TOTAL = {total}")
else:
    print("tipo inválido")


