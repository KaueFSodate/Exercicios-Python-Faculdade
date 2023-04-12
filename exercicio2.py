## Faça um programa que percorra todos os caracteres do nome, digitado pelo usuário, e o soletre.

texto = input("Insira um texto: ")

novo_texto = ''

for letra in texto: ## Cria a variavel letra no for.

    novo_texto += f'{letra}'
    print(letra)

print(novo_texto)