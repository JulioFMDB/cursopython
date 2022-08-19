# Exercicio 19
# Receba 4 nomes e faça um sorteio sobre eles
import random

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
n5 = input('Digite o quinto nome: ')
n6 = input('Digite o sexto nome: ')
lista = [n1,n2,n3,n4,n5,n6]
esc = random.choice(lista)
print('O aluno escolhido foi {}'.format(esc))