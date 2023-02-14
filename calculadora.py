from funcalc import *

while True:
    n1 = float(input('Insira o primeiro número: '))
    n2 = float(input('Insira o segundo número: '))
    operacao = str(input('Soma [+] / Subtração [-] / Multiplicação [*] / Divisão [/]\n')).strip().lower()
    if operacao == '+':
        print(f'{n1} + {n2} = {soma(n1, n2)}')
    if operacao == '-':
        print(f'{n1} - {n2} = {subtracao(n1, n2)}')
    if operacao == '*':
        print(f'{n1} * {n2} = {multiplicacao(n1, n2)}')
    if operacao == '/':
        print(f'{n1} / {n2} = {divisao(n1, n2)}')
    elif operacao not in '+-*/':
        print('Opção inválida!')

    continuar = str(input('Quer continuar? [s] / [n]\n')).lower()
    if continuar == 's':
        continue
    if continuar == 'n':
        break
    else:
        while continuar not in 'sn':
            continuar = str(input('Quer continuar? [s] / [n]\n')).lower()
            continuar = continuar
        if continuar == 'n':
            break

print('Fim')
