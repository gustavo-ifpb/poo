import json

# Leitura
f = open('pessoas.json', 'r')
pessoas = json.load(f)

selecionados = {'pessoas': []}

for pessoa in pessoas['pessoas']:
    op = input(f'Deseja selecionar a pessoa {pessoa["nome"]}? (s\\n) ')
    if op.lower() == 's':
        novaIdade = pessoa['idade'] + 10
        pessoaSelecionada = {
            'nome': pessoa['nome'],
            'e-mail': pessoa['email'],
            'idade': novaIdade
        }
        selecionados['pessoas'].append(pessoaSelecionada)
    
print(selecionados)
# Escrita
fout = open('pessoas_out.json', 'w')
json.dump(selecionados, fout)