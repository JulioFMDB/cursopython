from typing import ByteString
# Crie um script python que leia dois numeros e tente
# mostrar a soma entre eles

print ('Vamos somar dois numeros, siga os passos:')
a = float( input ('Digite o primeiro numero ' ))
b = float(input ('Digite o segundo numero ' ))

soma = a+b
#print ('a sua soma resultou em: ',soma)
print ('A soma entre {} e {} vale {}'.format(a,b,soma))