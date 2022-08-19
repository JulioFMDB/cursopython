#exercicio 18
# Faça um programa que leia um angulo qqr e mostre na tela o valor do
# seno, cosseno e tangente desse angulo
import math

a = float(input('Digite o angulo que voce quer saber seno, cosseno e tangente: ').replace(',','.'))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))

print ('O SENO deste angulo é {:.2f}'.format(seno))
print ('O COSSENO deste angulo é {:.2f}'.format(cosseno))
print ('A TANGENTE deste angulo é {:.2f}'.format(tangente))
