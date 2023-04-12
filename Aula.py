valor1 = input('digite: ')
valor2 = input('digite')

valor1int = int(valor1)
valor2int = int(valor2)

total = valor1int + valor2int

print(total)

# Python aulas Kaue.

#Função print.

print('ola mundo') #Tipo string pois tem ''

print(1) #Tipo inteiro pois tem 1

print(1.5) #Tipo float pois tem 1.5

print(7>5) #Tipo bool pois tem 1.5

#Convertendo tipos.

print(int('1') + 1) #Convertendo o '1' para 1
print(float('1.5') + 1) #Convertendo o '1.5' para 1.5
print(str(1) + 'b') #Convertendo o 1 para '1'

#Variaveis em Python.

nome = 'kaue'
idade = 19

print('O nome eh: ', nome, 'a idade eh: ', idade)

#Operadores aritmeticos.

adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

#f-Strings

print(f'O {nome} tem {idade} anos')

#Input para coletar dados

nomee = input('Digite o seu nome: ')
idadee = input('Digite a sua idade: ')

int_idade = int(idadee)

print(f'O seu nome eh {nomee} e voce tem {int_idade} anos')

#Estrutura condicionais

valor = 10

if valor >10:
    print('O valor eh maior que 10')
elif valor == 10:
    print('O valor eh igual a 10')
else:
    print('O valor eh menor que 10')

"""
Operadores de comparação (relacionais)

OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'

"""

# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor falso

# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor verdadeiro

# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nomeL = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nomeL, preco)


"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')


"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""


condicao = True

while condicao: #Se a condicao for true
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break #Sair do while se o nome for sair

print('Acabou')


contador = 0

while contador <= 5:
    contador += 1
    print(contador)

print('Acabou')

numero = 0

while numero <= 100:
    numero += 1

    if numero == 6:
        print('Não vou mostrar o 6.')
        continue

    if numero >= 10 and numero <= 15:
        print('Não vou mostrar o', numero)
        continue

    print(numero)

    if numero == 20:
        break


print('Acabou')


# for em python

texto = 'Python'

novo_texto = ''

for letra in texto: ## Cria a variavel letra no for.

    novo_texto += f'{letra}'
    print(letra)

print(novo_texto)

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

else:
    print('For completo com sucesso!')


"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)


#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[2] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))

"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))