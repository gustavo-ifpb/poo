with open('pessoas.csv', 'r') as f:
    # print(f.readlines())

    headers = f.readline().split(';')
    print(headers)

    for line in f:
        for i, data in enumerate(line.split(';')):
            print(f'{headers[i]}: {data}')