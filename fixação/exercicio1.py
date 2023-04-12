## Faça um programa que leia n valores fornecidos pelo usuário e calcule a soma de seus quadrados.

soma = 0

while True:
    valor = input('Insira um numero ou p para parar: ')

    if valor != 'p': ## Diferente de p ira somar o valor inserido
        soma += (float(valor) ** 2) #   soma = soma + (float(valor) ** 2)
    else:
        break
print(f'A soma dos quadrados dos valores eh: {soma}')