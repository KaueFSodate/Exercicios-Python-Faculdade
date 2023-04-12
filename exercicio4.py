## Sequencia fibonnaci com FOR

n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1
atual = 0

if (n==1) or (n==2):
    print("1")
else:
    for count in range(2,n):
        atual = ultimo + penultimo
        penultimo = ultimo
        ultimo = atual
        print(atual)