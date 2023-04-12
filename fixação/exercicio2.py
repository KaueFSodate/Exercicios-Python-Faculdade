## Faça um programa que leia n valores fornecidos pelo usuário e calcule a soma de seus quadrados.



while True:
    operacao = input('Insira uma operacão: ')
    if(operacao == 'soma'):
        num1 = input('Insira um numero para somar: ')
        num2 = input('Insira outro numero para somar: ')
        soma = int(num1) + int(num2)
        print(f'O resultado da soma eh: {soma}')
    elif(operacao == 'menos'):
        num1 = int(input('Insira um numero para subtrair: '))
        num2 = int(input('Insira outro numero para subtrair: '))
        menos = int(num1) - int(num2)
        print(f'O resultado da subtracao eh: {menos}')
    elif(operacao == 'multiplicar'):
        num1 = int(input('Insira um numero para multiplicar: '))
        num2 = int(input('Insira outro numero para multiplicar: '))
        multiplicar = int(num1) * int(num2)
        print(f'O resultado da soma eh: {multiplicar}')
    elif(operacao == 'dividir'):
        num1 = int(input('Insira um numero para dividir: '))
        num2 = int(input('Insira outro numero para dividir: '))
        dividir = int(num1) / int(num2)
        print(f'O resultado da dividisao eh: {dividir}')
    elif(operacao =='sair'):
        print('xau!')
        break

