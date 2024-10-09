# try:
#     print('Informe um número')
# except: 
#     print('Erro')


try:
    n = int(input('Informe um número: '))
except (ValueError, KeyboardInterrupt) as e:
    print(f'Erro: {e}')
else:
    print(f'Você informou {n}')

# try:
#     txt = input('Informe um nome: ')[0]
# except IndexError as e:
#     print(f"Precisa digitar algo")
# else:
#     print('Acertou')
# finally:
#     print('Sempre executar')
