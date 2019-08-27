import json

f = open('pessoas.json', 'r')
pessoas = json.load(f)
for pessoa in pessoas['pessoas']:
    print(f'Nome: {pessoa["nome"]}')