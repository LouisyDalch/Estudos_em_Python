soma = 0
count = 0
while True:
    num = int(input("Digite algum número, ou -1 para parar: "))
    if num == -1:
        break
    else:
        soma += num
        count += 1
print("Soma = ",soma)
print("Qtde = ",count," Números")
    
