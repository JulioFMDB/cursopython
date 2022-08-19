# Exercicio 05
# Capture um numero do usário e mostre seu sucessor e seu antecessor

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('O número digitado foi {}, seu anterior é {} e seu próximo é {}'.format(n,a,s))
# Poderia responder removendo as variaveis caso nao precisasse mais delas
# Então ficaria assim:
#print('O número digitado foi {}, seu anterior é {} e seu próximo é {}'.format(n,(n-1),(n+1)))
