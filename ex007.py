# Exercicio 007
# Faça um programa que leia duas notas de um aluno e mostre a média
print ('Programa de cáculo de media com duas notas: ')

n1 = float(input('Digite aqui a primeira nota do aluno: '))
n2 = float(input('Digite aqui a segunda nota do aluno: '))
n3 = (n1 + n2) / 2
print ('A nota 1 digitada foi: {:.2f}, a nota 2 foi: {:.2f}'.format(n1,n2))
print ('A média deste aluno é de {:.2f}'.format(n3))
