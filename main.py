from os import system, name
from time import sleep
import numpy as np


def limparConsole():
    system('cls' if name == 'nt' else 'clear')

def leiaInt(f):
    while True:
        try:
            resp = input(f)
            resp = int(resp)
        except ValueError:
            print('\033[1;31mDigite um número válido!\033[m')
            continue
        else:
            return resp


def verificarEquacao(tipoEq=0):
    if tipoEq == 0:
        while True:
            sistema = input("Digite a equação: ")
            if ('+' in sistema or '-' in sistema) and '=' in sistema:
                letra = list()
                for caractere in sistema:
                    if caractere.isalpha() and caractere not in ['-', '+'] and caractere not in letra:
                        letra.append(caractere)
                        if len(letra) == 2:
                            indice = sistema.index(letra[1])
                        
                if len(letra) != 2 or indice > sistema.index('='):
                    print('\033[1;31mEquação de sistema 2x2 inválida!\033[m')
                    sleep(1)
                else:
                    return sistema
            else:
                print('\033[1;31mEquação de sistema 2x2 inválida!\033[m')
                sleep(1)
    else:
        while True:
            sistema = input("Digite a equação: ")
            if ('+' in sistema or '-' in sistema) and '=' in sistema:
                letra = list()
                for caractere in sistema:
                    if caractere.isalpha() and caractere not in ['-', '+'] and caractere not in letra:
                        letra.append(caractere)
                        if len(letra) == 3:
                            indice = sistema.index(letra[1])
                        
                if len(letra) != 3 or indice > sistema.index('='):
                    print('\033[1;31mEquação de sistema 3x3 inválida!\033[m')
                else:
                    return sistema
            else:
                print('\033[1;31mEquação de sistema 3x3 inválida!\033[m')
    

def sistema2x2(*pLinhaEq, funcao=0):
    matriz = []
    incognitas = []
    numeros = []
    total = []
    pLinhaEq = str(pLinhaEq)
    pLinhaEq = pLinhaEq.replace('"', '').replace('(', '').replace(')', '')
    pLinhaEq = pLinhaEq.replace("'", '').split(',')
    for equacao in pLinhaEq:
        a = equacao.split('=')
        total.append(int(a[1].replace(' ', '')))
        b = a[0].replace(" ", "")
        lista = list()
        c = False
        index = list()
        indice = 0
        for i, valor in enumerate(b):
            if valor.isalpha() and valor not in ['-', '+'] and valor not in incognitas:
                incognitas.append(valor)
            if valor.isalpha() and valor not in ['-', '+']:
                index.append(int(b.index(incognitas[indice])))
                indice += 1
        for i in index:  
            if b[0:i].replace('+','') == '' or b[0:i] == '-' and i == index[0]:
                lista.append(int(b[0:i].replace('+','')+"1"))
            elif b[index[0]+1:i] == '-' or b[index[0]+1:i].replace('+','') == '' and i == index[1]:
                lista.append(int(b[index[0]+1:i].replace('+','')+ "1"))
            else:
                lista.append(int(b[0:i].replace('+',''))) if i == index[0] else lista.append(int(b[index[0]+1:i].replace('+','')))
        numeros.append(lista)
        index = list()
    matriz = [numeros, incognitas, total] 
    try:
        if funcao == 0:
            print(
            f'{"Indices ou A":^11}{" "*5}{"Incógnitas":^11}{"Total":^11}\n'
            f'|{matriz[0][0][0]:^5}{matriz[0][0][1]:^5}|{" "*5}|{matriz[1][0]:^5}|{" "*5}|{matriz[2][0]:^5}|\n'
            f'|{" "*10}|{"°":^5}|{" "*5}|{"=":^5}|{" "*5}|\n'
            f'|{matriz[0][1][0]:^5}{matriz[0][1][1]:^5}|{" "*5}|{matriz[1][1]:^5}|{" "*5}|{matriz[2][1]:^5}|\n')
            input('Aperte ENTER para continuar.')
            print('-' * 70)
            A = np.array(matriz[0])
            B = np.array([[matriz[2][0]], [matriz[2][1]]])
            A_inv = np.linalg.inv(A)
            X = np.linalg.solve(A, B)
            print(
            f'{"Matriz Inversa de A":^21}\n'
            f'|{A_inv[0][0]:^10.2f}{A_inv[0][1]:^10.2f}|\n'
            f'|{" " * 20}|\n'
            f'|{A_inv[1][0]:^10.2f}{A_inv[1][0]:^10.2f}|\n')
            input('Aperte ENTER para continuar.')
            print('-' * 70)
            print('Lembre-se multiplicação matricial NÃO é comutativa!\n')
            print(
            f'  {"Incógnitas":^8}{" "*5}{"Matriz Inversa de A":^21}{"Total":^16}\n'
            f'  |{matriz[1][0]:^5}|{" "*5}|{A_inv[0][0]:^10.2f}{A_inv[0][1]:^10.2f}|{" "*5}|{matriz[2][0]:^5}|\n'
            f'  |{" "*5}|{"=":^5}|{" "*20}|{"°":^5}|{" "*5}|\n'
            f'  |{matriz[1][1]:^5}|{" "*5}|{A_inv[1][0]:^10.2f}{A_inv[1][0]:^10.2f}|{" "*5}|{matriz[2][1]:^5}|\n')
            input('Aperte ENTER para continuar.')
            print('-' * 70)
            print('Resultado! :) \n')
            print(
            f'  {"Indices":^8}{" "*5}{"Valor":^11}\n'
            f'  |{matriz[1][0]:^5}|{" "*5}|{X[0][0]:^10.4f}|\n'
            f'  |{" "*5}|{"=":^5}|{" "*10}|\n'
            f'  |{matriz[1][1]:^5}|{" "*5}|{X[1][0]:^10.4f}|\n')
        elif funcao == 1:
            A = np.array(matriz[0])
            B = np.array([[matriz[2][0]], [matriz[2][1]]])
            X = np.linalg.solve(A, B)
            print(f'{" Resultado! ":-^70}')
            print(
            f'{matriz[1][0].upper()} = {X[0][0]:.4f}\n'
            f'{matriz[1][1].upper()} = {X[1][0]:.4f}\n')
            sleep(2)
    except:
        print("\033[1;31mAconteceu um erro inesperado! Verifique as equações e tente novamente!\033[m")
        
        
def sistema3x3(*pLinhaEq, funcao = 0):
    matriz = []
    incognitas = []
    numeros = []
    total = []
    pLinhaEq = str(pLinhaEq)
    pLinhaEq = pLinhaEq.replace('"', '').replace('(', '').replace(')', '')
    pLinhaEq = pLinhaEq.replace("'", '').split(',')
    for equacao in pLinhaEq:
        a = equacao.split('=')
        total.append(int(a[1].replace(' ', '')))
        b = a[0].replace(" ", "")
        lista = list()
        c = False
        index = list()
        indice = 0
        for i, valor in enumerate(b):
            if valor.isalpha() and valor not in ['-', '+'] and valor not in incognitas:
                incognitas.append(valor)
            if valor.isalpha() and valor not in ['-', '+']:
                index.append(int(b.index(incognitas[indice])))
                indice += 1
        for i in index:
            if b[0:i].replace('+','') == '' or b[0:i] == '-' and i == index[0]:
                lista.append(int(b[0:i].replace('+','')+"1"))
            elif b[index[0]+1:i] == '-' or b[index[0]+1:i].replace('+','') == '' and i == index[1]:
                lista.append(int(b[index[0]+1:i].replace('+','')+ "1"))
            elif b[index[1]+1:i] == '-' or b[index[1]+1:i].replace('+','') == '' and i == index[2]:
                lista.append(int(b[index[1]+1:i].replace('+','')+ "1"))
            else:
                if i == index[0]:
                    lista.append(int(b[0:i].replace('+','')))  
                elif i == index[1]:
                    lista.append(int(b[index[0]+1:i].replace('+','')))
                else:
                    lista.append(int(b[index[1]+1:i].replace('+','')))
        numeros.append(lista)
        index = list()
    matriz = [numeros, incognitas, total] 
    try:
        if funcao == 0:
            print(
            f'{"Indices ou A":^17}{" "*5}{"Incógnitas":^8}{"Total":^13}\n'
            f'|{matriz[0][0][0]:^5}{matriz[0][0][1]:^5}{matriz[0][0][2]:^5}|{" "*5}|{matriz[1][0]:^5}|{" "*5}|{matriz[2][0]:^6}|\n'
            f'|{" "*15}|{" "*5}|{" "*5}|{" "*5}|{" "*6}|\n'
            f'|{matriz[0][1][0]:^5}{matriz[0][1][1]:^5}{matriz[0][1][2]:^5}|{"°":^5}|{matriz[1][1]:^5}|{"=":^5}|{matriz[2][1]:^6}|\n'
            f'|{" "*15}|{" "*5}|{" "*5}|{" "*5}|{" "*6}|\n'
            f'|{matriz[0][2][0]:^5}{matriz[0][2][1]:^5}{matriz[0][2][2]:^5}|{" "*5}|{matriz[1][2]:^5}|{" "*5}|{matriz[2][2]:^6}|\n')
            input('Aperte ENTER para continuar.')
            print('-' * 70)
            A = np.array(matriz[0])
            B = np.array([[matriz[2][0]], [matriz[2][1]], [matriz[2][2]]])
            A_inv = np.linalg.inv(A)
            X = np.linalg.solve(A, B)
            print(
            f'{"Matriz Inversa de A":^30}\n'
            f'|{A_inv[0][0]:^10.2f}{A_inv[0][1]:^10.2f}{A_inv[0][2]:^10.2f}|\n'
            f'|{" " * 30}|\n'
            f'|{A_inv[1][0]:^10.2f}{A_inv[1][1]:^10.2f}{A_inv[1][2]:^10.2f}|\n'
            f'|{" " * 30}|\n'
            f'|{A_inv[2][0]:^10.2f}{A_inv[2][1]:^10.2f}{A_inv[2][2]:^10.2f}|\n')
            input('Aperte ENTER para continuar.')
            print('-' * 70)
            print('Lembre-se multiplicação matricial NÃO é comutativa!\n')
            print(
            f'  {"Incógnitas":^7}{" "*5}{"Matriz Inversa de A":^28}{"Total":^17}\n'
            f'  |{matriz[1][0]:^5}|{" "*5}|{A_inv[0][0]:^10.2f}{A_inv[0][1]:^10.2f}{A_inv[0][2]:^10.2f}|{" "*5}|{matriz[2][0]:^5}|\n'
            f'  |{" "*5}|{" "*5}|{" "*30}|{" "*5}|{" "*5}|\n'
            f'  |{matriz[1][1]:^5}|{"=":^5}|{A_inv[1][0]:^10.2f}{A_inv[1][1]:^10.2f}{A_inv[1][2]:^10.2f}|{"°":^5}|{matriz[2][1]:^5}|\n'
            f'  |{" "*5}|{" "*5}|{" "*30}|{" "*5}|{" "*5}|\n'
            f'  |{matriz[1][2]:^5}|{" "*5}|{A_inv[2][0]:^10.2f}{A_inv[2][1]:^10.2f}{A_inv[2][2]:^10.2f}|{" "*5}|{matriz[2][2]:^5}|\n')
            input('Aperte ENTER para continuar.')
            print('-' * 70)
            print('Resultado! :) \n')
            print(
            f'  {"Incógnitas":^7}{" "*5}{"Valor":^11}\n'
            f'    |{matriz[1][0]:^5}|{" "*5}|{X[0][0]:^10.4f}|\n'
            f'    |{" "*5}|{" "*5}|{" "*10}|\n'
            f'    |{matriz[1][1]:^5}|{"=":^5}|{X[1][0]:^10.4f}|\n'
            f'    |{" "*5}|{" "*5}|{" "*10}|\n'
            f'    |{matriz[1][2]:^5}|{" "*5}|{X[2][0]:^10.4f}|\n')
        else:
            A = np.array(matriz[0])
            B = np.array([[matriz[2][0]], [matriz[2][1]], [matriz[2][2]]])
            X = np.linalg.solve(A, B)
            print(f'{" Resultado! ":-^70}')
            print(
            f'{matriz[1][0].upper()} = {X[0][0]:.4f}\n'
            f'{matriz[1][1].upper()} = {X[1][0]:.4f}\n'
            f'{matriz[1][2].upper()} = {X[2][0]:.4f}\n')
            sleep(2)
    except:
        print("\033[1;31mAconteceu um erro inesperado! Verifique as equações e tente novamente!\033[m")




while True:
    print(f'{" Calculadora de equações lineares ":-^70}\n')
    print('''Escolha o tamanho do sistema\n
[ 1 ] \033[1;31m2x2\033[m
[ 2 ] \033[1;32m3x3\033[m
[ 3 ] Sair do programa
''')
    print('-' * 70)
    escolha = leiaInt('Sua opção: ')
    if escolha == 1:
        limparConsole()
        print(f'{" Sistema 2x2 ":-^70}')
        print('''
[ 1 ] Passo a Passo
[ 2 ] Cálculo Direto (Apenas o resultado)
[ 3 ] Voltar
        ''')
        print('-' * 70)
        escolhaSistema = leiaInt('Sua opção: ')
        if escolhaSistema == 1:
            limparConsole()

            sistema1 = verificarEquacao()
            sistema2 = verificarEquacao()
            sistema2x2(sistema1, sistema2)
        elif escolhaSistema == 2:
            limparConsole()

            sistema1 = verificarEquacao()
            sistema2 = verificarEquacao()
            sistema2x2(sistema1, sistema2, funcao=1)
        elif escolhaSistema == 3:
            limparConsole()

            continue
        else:
            print('Escolha inválida!')
            sleep(1)
            limparConsole()

    elif escolha == 2:
        limparConsole()
        print(f'{" Sistema 3x3 ":-^70}')
        print('''
[ 1 ] Passo a Passo
[ 2 ] Cálculo Direto (Apenas o resultado)
[ 3 ] Voltar
        ''')
        print('-' * 70)
        escolhaSistema = leiaInt('Sua opção: ')
        if escolhaSistema == 1:
            limparConsole()

            sistema1 = verificarEquacao(1)
            sistema2 = verificarEquacao(1)
            sistema3 = verificarEquacao(1)
            sistema3x3(sistema1, sistema2, sistema3, funcao=0)
        elif escolhaSistema == 2:
            limparConsole()

            sistema1 = verificarEquacao(1)
            sistema2 = verificarEquacao(1)
            sistema3 = verificarEquacao(1)
            sistema3x3(sistema1, sistema2, sistema3, funcao=1)
        elif escolhaSistema == 3:
            limparConsole()

            continue
        else:
            print('Escolha inválida!')
            sleep(1)
            limparConsole()

    elif escolha == 3:
        print('Saindo...')
        sleep(2)
        limparConsole()
        break
    else:
        print("Opção inválida!")
        sleep(1)
        limparConsole()
    
print('''\033[1;33m
 (                           )     (                     
 )\ )             (       ( /(     )\ )                  
(()/(      (      )\      )\())   (()/(    (     (   (   
 /(_))     )\  ((((_)(   ((_)\     /(_))   )\    )\  )\  
(_))    _ ((_)  )\ _ )\   _((_)   (_))_   ((_)  ((_)((_) 
| |    | | | |  (_)_\(_) | \| |    |   \  | __| \ \ / /  
| |__  | |_| |   / _ \   | .` |    | |) | | _|   \ V /   
|____|  \___/   /_/ \_\  |_|\_|    |___/  |___|   \_/\033[m    
                                                        
github.com/Luan-FlavioBr
''')
