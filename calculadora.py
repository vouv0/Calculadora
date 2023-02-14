while True:
    n1 = float(input('Insira o primeiro número: '))
    n2 = float(input('Insira o segundo número: '))
    operacao = str(input('Soma [+] / Subtração [-] / Multiplicação [*] / Divisão [/]\n')).strip().lower()
    if operacao == '+':
        resultado = n1 + n2
        print(f'{n1} + {n2} = {resultado}')
    if operacao == '-':
        resultado = n1 - n2
        print(f'{n1} - {n2} = {resultado}')
    if operacao == '*':
        resultado = n1 * n2
        print(f'{n1} * {n2} = {resultado}')
    if operacao == '/':
        resultado = n1 / n2
        print(f'{n1} / {n2} = {resultado}')
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
