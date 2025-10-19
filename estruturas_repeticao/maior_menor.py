'''
3 - Escreva um programa que leia uma sequência de números inteiros e positivos,
encontre e imprima o maior e o menor número. A entrada de um número negativo indica que
a sequência terminou.
'''
n=int(input("Digite um número: "))
seq=""
while True:
   num=int(input("Digite outro número: "))
   if n>0 and num>0:
        if n>=num:
            if n==num:
                print("são iguais")
            else:
                print(n," é maior")   
        else:
           print(num," é maior")
           n=num
        seq += f"{num},"
   else:
       seq += "FIM"
       break
print(seq)
