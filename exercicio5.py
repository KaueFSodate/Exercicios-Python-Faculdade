## Sequencia fibonnaci com WHILE

n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1
atual = 0
interacoes = 1

if (n==1) or (n==2):
    print("1")
else:
    while interacoes <= 2:
        if (interacoes<=2):
            print("1", end=',')
        else:
            atual = ultimo + penultimo
            penultimo = ultimo
            ultimo = atual

            print(atual, end=',')
        interacoes += 1