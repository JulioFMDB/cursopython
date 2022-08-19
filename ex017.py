#Exercicio 17
#Faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente
# de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

from math import hypot

co = float(input('Digite o valor do cateto oposto: ').replace(',','.'))
ca = float(input('Digite o valor do cateto adjacente: ').replace(',','.'))
#hi = (co ** 2 + ca **2) ** (1/2)
#print ('A hipotenusa vai medir {:.2f}'.format(hi))
hi = hypot(co,ca)
print ('A hipotenusa vai medir {:.2f}'.format(hi))