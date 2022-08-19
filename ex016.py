#execrcico 16
# Crie um programa que leia um numero real, e mostre na tela sua porção inteira

from math import floor

n = float (input('Digite o numero para saber seu inteiro: ').replace(',','.'))
print('O número digitado foi {}, sua porção inteira é {}'.format(n,floor(n)))