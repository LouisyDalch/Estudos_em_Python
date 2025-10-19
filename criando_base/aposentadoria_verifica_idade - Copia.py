'''A aposentadoria é um direito concedido a todos os contribuintes do INSS, desde que cumpram alguns requisitos impostos pela legislação,
que variam de acordo com o tipo de aposentadoria escolhido pelo segurado.
Os requisitos envolvem a idade e o tempo de serviço do trabalhador. As condições para aposentadoria são:

 - Ter pelo menos 65 anos,

 - Ou ter trabalhado pelo menos 30 anos,

 - Ou ter pelo menos 60 anos e ter trabalhado pelo menos 25 anos.'''

idade = int(input("Digite sua idade: "))
trabalhados = int(input("Digite a quantidade de anos trabalhados que você tem: "))
if(idade >= 65):
    print("Você está apto para se aposentar!")
elif(trabalhados >= 30):
    print("Você está apto para se aposentar!")
elif(idade >= 60 and trabalhados >= 25):
    print("Você está apto para se aposentar!")
else:
    print("Você não está apto para se aposentar!")
