##  Peça 5 valores de qualquer tipo para o usuário, guarde na em uma lista, em seguida imprima-os.

numeros= []
maior = menor = meio = 0

for i in range (0, 5):
    num = int(input("Digite um número: "))
    if i == 0:
        maior = menor = num
        numeros.append(num)
    elif num >= maior:
        maior = num
        numeros.append(num)
    elif num <= menor:
        menor = num
        numeros.insert(0, num)
    elif menor < num < maior:
        if meio == 0:
            meio = num
            numeros.insert(menor < num < maior, num)
        elif meio <= num:
            numeros.insert(meio < num < maior, num)
            meio = num
        elif meio >= num:
            numeros.insert(menor < num < meio, num)
print(numeros)