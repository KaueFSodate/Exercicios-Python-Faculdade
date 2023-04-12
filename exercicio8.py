##  Ler uma lista de 10 números reais e mostre-os na ordem inversa.

numeros= []
maior = menor = meio = 0

for i in range (0, 10):
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
numeros.reverse()
print(numeros)
