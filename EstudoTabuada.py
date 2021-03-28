from time import sleep
from random import randint
import os
nome_prog = 'Estudar Tabuada 1.0'


# Função que chama o comando 'CLS' para limpar o prompt
def limpar_tela():
    os.system('cls')


# Função que gera o menu e pergunta qual opção desejar escolher
def menu():
    global opcao
    print('\033[1;97m-=\033[m' * 30)
    print(f'\033[1;32m{nome_prog:^60}\033[m')
    print('\033[1;97m-=\033[m' * 30)
    print(f'\033[1;32;4m{"Escolha a opção desejada:"}\033[m', end=' ')
    print('''
    \033[97m[\033[m\033[1;31m1\033[m\033[97m]\033[m \033[1;97mExibir Tabuadas\033[m
    \033[97m[\033[m\033[1;31m2\033[m\033[97m]\033[m \033[1;97mTeste seu Conhecimento\033[m
    \033[97m[\033[m\033[1;31m3\033[m\033[97m]\033[m \033[1;97mEncerra o Programa\033[m
    ''')
    while True:
        try:
            opcao = int(input('Digite a opção desejada: '))
            if opcao == 1 or opcao == 2 or opcao == 3:
                break
            else:
                print('Opção Inválida, tenta novamente!')
        except ValueError:
            print('Opção Inválida, tenta novamente!')


# Função que cria e exibe ordenadamente as tabuadas de 1 até 10
def exibir_tabuadas():
    print('\033[1;33m~\033[m' * 85)
    print(f'\033[1;34m{"TABUADAS":^85}\033[m')
    print(f'\033[97m{"Estude para ser o melhor e vencer!!":^85}\033[m')
    print('\033[1;33m~\033[m' * 85)
    print()
    for v in range(0, 11):
        for h in range(0, 1):
            print(f'\033[1;97m{1:>2} x {v:>2}\033[m = \033[1;32m{1 * v:>3}\033[m', end='  |  ')
            print(f'\033[1;97m{2:>2} x {v:>2}\033[m = \033[1;32m{2 * v:>3}\033[m', end='  |  ')
            print(f'\033[1;97m{3:>2} x {v:>2}\033[m = \033[1;32m{3 * v:>3}\033[m', end='  |  ')
            print(f'\033[1;97m{4:>2} x {v:>2}\033[m = \033[1;32m{4 * v:>3}\033[m', end='  |  ')
            print(f'\033[1;97m{5:>2} x {v:>2}\033[m = \033[1;32m{5 * v:>3}\033[m')
    print()
    for v in range(0, 11):
        for h in range(0, 1):
            print(f'\033[1;97m{6:>2} x {v:>2}\033[m = \033[1;32m{6 * v:>3}\033[m', end='  |  ')
            print(f'\033[1;97m{7:>2} x {v:>2}\033[m = \033[1;32m{7 * v:>3}\033[m', end='  |  ')
            print(f'\033[1;97m{8:>2} x {v:>2}\033[m = \033[1;32m{8 * v:>3}\033[m', end='  |  ')
            print(f'\033[1;97m{9:>2} x {v:>2}\033[m = \033[1;32m{9 * v:>3}\033[m', end='  |  ')
            print(f'\033[1;97m{10:>2} x {v:>2}\033[m = \033[1;32m{10 * v:>3}\033[m')
    print()
    print('\033[1;33m~\033[m' * 85)


# Cria o submenu do teste de conhecimento e trata possiveis erros
def menu_conhecimento():
    global tipo
    print('\033[1;97m-=\033[m' * 30)
    print(f'\033[1;32;4m{"Escolha a opção desejada:"}\033[m', end='')
    print('''
    \033[97m[\033[m\033[1;31m1\033[m\033[97m]\033[m \033[1;97mEscolha a tabuada que deseja fazer o teste\033[m
    \033[97m[\033[m\033[1;31m2\033[m\033[97m]\033[m \033[1;97mExecuta o teste aleatoriamente\033[m
    \033[97m[\033[m\033[1;31m3\033[m\033[97m]\033[m \033[1;97mVolta ao Menu Princial\033[m''')
    print('\033[1;97m-=\033[m' * 30)
    while True:
        try:
            tipo = int(input('Digite a opção desejada: '))
            if tipo == 1 or tipo == 2 or tipo == 3:
                break
            else:
                print('Opção Inválida, tenta novamente!')
        except ValueError:
            print('Opção Inválida, tenta novamente!')
    return tipo


def teste_conhecimento():
    while True:
        tipo = menu_conhecimento()
        if tipo == 1:
            # Pergunta qual tabuada o usuário deseja fazer o teste e faz o tratamento de erros
            while True:
                try:
                    escolha = int(input('\033[1;97mDigite a tabuada que deseja fazer o teste\033[m \033[1;31m[1 até 10]\033[m: '))
                    if escolha >= 1 and escolha <= 10:
                        break
                    else:
                        print('Opção Inválida, tenta novamente!')
                except ValueError:
                    print('Opção Inválida, tenta novamente!')
            # Gera 6 perguntas aleatórias da tabuada escolhida, eliminando a possibilidade de perguntas repetidas
            repetidas = []
            resultado = []
            x = 0
            print('\033[1;33m*\033[m' * 60)
            print('\033[1;32mVamos lá, boa sorte!\033[m')
            print('\033[1;97mResponda as perguntas abaixo: \033[m')
            for c in range(0, 6):
                while x in repetidas:
                    x = randint(0, 10)
                repetidas.append(x)
                perg = str(escolha) + str(' x ') + str(f'{x:>2}')
                verf = escolha * x
                while True:
                    try:
                        resp = int(input(f'{c + 1}ª pergunta: {escolha:>2} x {x:>2} = '))
                        break
                    except ValueError:
                        print('Um valor precisa ser digitado!')
                if verf == resp:
                    status = 'Certa'
                else:
                    status = 'Errada'
                lista_temp = [c+1, perg, resp, status, verf]
#                lista_temp = [c+1, escolha, x, resp, status, verf]
                resultado.append(lista_temp[:])
                lista_temp.clear()
            print('\033[1;33m*\033[m' * 60)
            print('\033[1;97mAnálisando seu resultado ...\033[m')
            tot_ac = 0
            for p in resultado:
                print(f'{p[0]}ª pergunta: {p[1]} = ', flush=True, end='')
                sleep(0.5)
                print(f'{p[2]:>2} ', flush=True, end='')
                sleep(0.5)
                print('-', flush=True, end='')
                sleep(0.5)
                print('-', flush=True, end='')
                sleep(0.5)
                print('> ', flush=True, end='')
                sleep(0.5)
                if p[3] == 'Certa':
                    print(f'\033[1;32m {p[3]}\033[m', flush=True)
                    tot_ac += 1
                else:
                    print(f'\033[1;31m{p[3]}\033[m', flush=True, end='')
                    sleep(0.5)
                    print(f' >> Resposta correta é: ', flush=True, end='')
                    sleep(1)
                    print(f'\033[1;32m{p[4]}\033[m', flush=True)
            print()
            print('\033[1;33m-\033[m' * 60, flush=True)
            print('\033[1;33mResumo:\033[m ')
            print(f'\033[1;97mVocê acertou\033[m \033[1;34m{tot_ac}\033[m \033[1;97mresposta, com um aproveitamento de'
                  f'\033[1;34m {(tot_ac/6)*100:.1f}%\033[m\033[1;97m.\033[m')
            if (tot_ac / 6) >= 0.7:
                print(f'\033[1;32mParabéns, você foi muito bem, continue estudando!!\033[m')
            else:
                print(f'\033[1;31mVocê precisa estudar mais, NUNCA DESISTA!\033[m')
            print('\033[1;33m-\033[m' * 60, flush=True)
            print()
            sleep(2)
            voltar()
            print()
        elif tipo == 2:
            print('em construção')
        elif tipo == 3:
            break


# Função que faz o teste aleatório de 10 perguntas
def teste_aleatorio():
    tab = []


def voltar():
    while True:
        try:
            v = int(input(f'Digite \033[1;31m1\033[m para voltar ao MENU PRINCIPAL: '))
            if v == 1:
                break
            else:
                print('Opção Inválida, tenta novamente!')
        except ValueError:
            print('Opção Inválida, tenta novamente!')


# Programa Principal
while True:
    limpar_tela()
    menu()
    if opcao == 1:
        limpar_tela()
        exibir_tabuadas()
        voltar()
        limpar_tela()
    elif opcao == 2:
        limpar_tela()
        teste_conhecimento()
    elif opcao == 3:
        print('\033[1;31m-=\033[m' * 30)
        print('\033[1;32m   VOLTE SEMPRE -->\033[m \033[1;97mNunca se esqueça de estudar bastante!\033[m')
        print(f'\033[1;32m{"PROGRAMA ENCERRADO!":^60}\033[m')
        print('\033[1;31m-=\033[m' * 30)
        sleep(2)
        break
