from Mini_Sistema.lib.interface import *

def arqExiste(msg):
    '''

    :param msg: Um arquivo que deseja encontrar
    :return: Retorna se o arquivo existe ou não
    '''
    try:
        a = open(msg, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(msg):
    '''

    :param msg: O nome do arquivo que deseja criar
    :return: Retorna criando um arquivo desejado
    '''
    try:
        a = open(msg, 'wt+')
        a.close()
    except:
        print('Houve um erro ao tentar criar o arquivo.')
    else:
        print(f'Arquivo {msg} criado com sucesso!')


def lerArq(msg):
    '''

    :param msg: O nome do arquivo que deseja ler
    :return: Retorna a vizualização dos itens do arquivo
    '''
    try:
        a = open(msg, 'rt')
    except:
        print('Hove algum erro ao tentar abrir o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(msg, n='Desconhecido', i=0):
    '''

    :param msg: O nome do arquivo que deseja editar
    :param n: O nome de uma pessoa que deseja adicionar a lista
    :param i: A idade da pessoa adicionada a lista
    :return: Retorna se a pessoa foi adiciona com êxito ou não
    '''
    try:
        a = open(msg, 'at')
    except:
        print('Houve um erro ao tentar abrir o arquivo.')
    else:
        try:
            a.write(f'{n};{i}\n')
        except:
            print('Houve um ERRO! na hora de escrever os dados.')
        else:
            print(f'Novo registro de {n} adicionado.')
            a.close()

