# Fazer um programa que leia um numero inteiro e dizer se ele é primo

num = int(input ('Digite um numero inteiro pra saber se é primo: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('', end='')
        total +=1
    else:
        print (' ', end='')
    print ('{}'.format(c), end ='')
print('\nO numero {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print ('É primo')
else:
    print ('nao é primo')