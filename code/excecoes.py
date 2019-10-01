sexo = input('Digite seu sexo: (m/f)')
if sexo.lower() == 'm':
    print('Masculino')
elif sexo.lower() == 'f':
    print('Feminino')
else:
    raise Exception('Sexo informado diferente de M/F')







# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError:
#     print('Arquivo não encontrado!')
# except ValueError:
#     i = None
#     print('Não foi possível converter para inteiro!')
# except:
#     print('Exceção desconhecida!')
# print(i)

# while True:
#     try:
#         x = int(input('Digite um número: '))
#         break
#     except ValueError:
#         print('eita!')
#     except:
#         print('opa!')