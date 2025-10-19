#EXERCÍCIO 3
import math
alt = float(input("Digite a altura da lata! "))
r = float(input("Digite o raio da lata! "))
v = alt*r**2*math.pi

print("Volume da lata: ", format(v,".2f"))
