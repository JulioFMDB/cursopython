# Exercicio 20
# sorteie a ordem dos nomes anteriores
import random

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
n5 = input('Digite o quinto nome: ')
n6 = input('Digite o sexto nome: ')
lista = [n1,n2,n3,n4,n5,n6]
random.shuffle(lista)
print ('A ordem é: ')
print(lista)