from Mini_Sistema.lib.interface import *
from Mini_Sistema.lib.arquivo import *
from time import sleep

arq = 'sistema.txt'
if arqExiste(arq):
    print('Arquivo encontrado com sucesso')
else:
    criarArq(arq)
cabeçalho('MENU PRINCIPAL')
while True:
    r = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if r == 0:
        lerArq(arq)
        print(l())
        sleep(1)
    elif r == 1:
        cabeçalho('NOVO CADASTRO')
        n = str(input('Nome: '))
        i = leiaInt('Idade: ')
        cadastrar(arq, n, i)
        print(l())
        sleep(1)
    elif r == 2:
        print(l())
        print(f'{"   Saindo do Sistema"}', end='')
        for c in range(0, 3):
            print('.', end='')
            sleep(1)
        print(' Finalizado! Até logo!!')
        print(l())
        sleep(2)
        break
    else:
        cabeçalho('\033[31mERRO!! Digite uma opção válida.')
        sleep(1)
