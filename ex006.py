# Exercicio 006
# Fazer um programa que leia um numero e de o seu dobro, triplo e sua raiz quadrada.

from math import sqrt
n = int (input('Digite um número para saber seu dobro, triplo e raiz quadrada: '))

n1 = n * 2
n2 = n * 3
n3 = sqrt(n) #poderia usar n2 = n ** (1/2), sem chamar a biblioteca math
print ('O número que você digitou foi {}'.format(n))
print(' ')
print ('O dobro de {} é {}'.format(n,n1))
print ('O triplo de {} é {}'.format(n,n2))
print ('A raiz quadrada de {} é {:.2f}'.format(n,n3))
