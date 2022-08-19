# Exercicio 008
# Faça um programa que leia um valor em metros, e o exiba
# em centimetros e milimetros.
print ('Programa conversor de medidas: ')
print ('\n')
m = float (input('Digite aqui o valor em metros: ').replace(',','.'))
cm = m * 100
mm = cm * 10
print ('O valor em metros digitado é: {}'.format(m))
print ('{} metros é igual a {:.2f} cm'.format(m,cm))
print ('{} metros equivalem a {:.2f} mm'.format(m,mm))
