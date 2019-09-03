# Leitura
with open('pessoas.csv', 'r') as f:
    # print(f.readlines())

    headers = f.readline().split(';')
    print(headers)

    selecionados = []

    for line in f:
        data = line.split(';')
        op = input(f'Deseja selecionar a pessoa {data[0]}? (s\\n) ')
        if op.lower() == 's':
            selecionados.append('{};{}'.format(data[0], data[2]))

        # for i, data in enumerate(line.split(';')):
        #     print(f'{headers[i]}: {data}')

# Escrita
with open('pessoas_out.csv', 'w') as fout:
    # Header
    fout.write('Nome;E-mail\n')
    for selecionado in selecionados:
        fout.write(selecionado)
        fout.write('\n')
    fout.close()