from Mini_Sistema.lib.cores import *
from time import sleep
def leiaInt(msg):
    '''

    :param msg: Texto exibido na pergunta.
    :return: Retorna um valor Inteiro
    '''
    try:
        n = int(input(msg))
    except (ValueError, TypeError):
        while True:
            print('\033[31mERRO!!: Por favor, digite um inteiro válido.\033[m')
            n = str(input('Digite um Inteiro: '))
            if n.isnumeric():
                n = int(n)
                break
    except KeyboardInterrupt:
        print('\033[31mO usuário preferio não informar o valor.\033[m')
    finally:
        return n

def l(tam=50):
   return '-' * tam



def cabeçalho(msg):
    '''

    :param msg: Uma mensagem para cabeçalho
    :return: Retorna um cabeçalho editado
    '''
    print(l())
    print(f'{msg:^50}')
    print(l())


def menu(lista):
    '''

    :param lista: Uma lista de 3 itens para escolha
    :return: Retorna editado 3 itens em formato de lista para orientação
    '''
    for c, v in enumerate(lista):
        print(f'\033[33m{c} -\033[m \033[34m{v}\033[m')
    print(l())
    opc = leiaInt('\033[33mSua opção:\033[m ')
    return opc


def go():
    '''

    :return: Retorna a palavra JO KEN PÔ com pausas de 1seg
    '''
    print(f'{green():>23}JO', end='  ')
    sleep(1)
    print(f'KEN', end='  ')
    sleep(1)
    print(f'PÔ!{semCor()}')
    print(l())


def condWin(c, p):
    '''

    :param c: Recebe a jogada do computador
    :param p: Recebe a jogada do player
    :return: Retorna quem ganhou
    '''
    if c == 0:
        if p == 0:
            cabeçalho(f'{yellow()}{"DEU EMPATE!!":>7}{semCor()}')
        elif p == 1:
            cabeçalho(f'{green()}{"JOGADOR VENCEU!!":>6}{semCor()}')
        elif p == 2:
            cabeçalho(f'{red()}{"O COMPUTADOR VENCEU!!":>5}{semCor()}')
    elif c == 1:
        if p == 0:
            cabeçalho(f'{red()}     O COMPUTADOR VENCEU!!{semCor()}')
        elif p == 1:
            cabeçalho(f'{yellow()}       DEU EMPATE!!{semCor()}')
        elif p == 2:
            cabeçalho(f'{green()}      O JOGADOR VENCEU!!{semCor()}')
    elif c == 2:
        if p == 0:
            cabeçalho(f'{green()}      O JOGADOR VENCEU!!{semCor()}')
        elif p == 1:
            cabeçalho(f'{red()}     O COMPUTADOR VENCEU!!{semCor()}')
        elif p == 2:
            cabeçalho(f'{yellow()}       DEU EMPATE!!{semCor()}')



