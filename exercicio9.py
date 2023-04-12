##  Ler uma lista de 10 números reais e mostre-os na ordem inversa.

notas= []
maior = menor = meio = 0

for i in range (0, 4):
    num = int(input("Digite um número: "))
    if i == 0:
        maior = menor = num
        notas.append(num)
    elif num >= maior:
        maior = num
        notas.append(num)
    elif num <= menor:
        menor = num
        notas.insert(0, num)
    elif menor < num < maior:
        if meio == 0:
            meio = num
            notas.insert(menor < num < maior, num)
        elif meio <= num:
            notas.insert(meio < num < maior, num)
            meio = num
        elif meio >= num:
            notas.insert(menor < num < meio, num)
listaSoma = sum(notas)
listaSomaMedia = listaSoma / 4
print(f'As notas sao: {notas} e media eh: {listaSomaMedia}')
