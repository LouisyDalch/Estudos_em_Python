#EXERCÍCIO 5
import math
custo = float(input("Digite o valor do espetáculo: "))
ingre = float(input("Digite o valor do ingresso: "))
qtd_ingre1 = math.ceil(custo / ingre)

print("Quantidade de ingressos a serem vendidos para alcançar o custo do espetáculo: ", qtd_ingre1)

lucro = custo *1.23

print(f"Valor com o lucro: {lucro:.2f}")
qtd_ingre2 = math.ceil(lucro / ingre)

print("Quantidade de ingressos a serem vendidos para alcançar um lucro de 23%: ", qtd_ingre2)
