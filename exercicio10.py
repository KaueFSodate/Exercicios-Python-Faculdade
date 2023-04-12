## Crie um programa que peça para o usuário: nome, telefone, email
nome = input('Insira um nome: ')
telefone = input('Insira o primeiro telefone: ')
telefone2 = input('Insira o segundo telefone: ')
email = input('Insira um email: ')


d4['contatos'] = {'usuario': {
        nome: {
            'telefone1': telefone,
            'telefone2': telefone2,
            'email': email,

        }
    }
} 

# Percorrendo um dicionário

for key, value in d4.items():
    print(f'{key} - {value}\n')

Nome = input('Pesquise por nome: ')

# Pesquisando por nome específico
print(d4.get(Nome, 'Não encontrado'))