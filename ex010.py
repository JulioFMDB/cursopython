# Crie um programa converta reais em dólares
import requests
import json
requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
r = float(input('Digite o valor em reais: '))