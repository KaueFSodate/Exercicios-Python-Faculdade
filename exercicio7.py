##  Faça um programa que sorteie 10 números de 1 a 10, guarde-os em uma lista, e mostre o valor que foi sorteado mais vezes.

import random
for c in range (1, 10):
    n1 = str(input("Digite um nº: "))
l = [n1]
random.shuffle(l)
print("Números escolhidos: ", l)
