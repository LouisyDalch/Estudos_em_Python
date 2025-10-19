empr_querido = float(input("Quanto você gostaria? "))
salario = float(input("Quanto você ganha? "))

if(empr_querido > salario*0.2):
    print("Não é possível fazer esse empréstimo!")
else:
    print("Empréstimo concedido")
