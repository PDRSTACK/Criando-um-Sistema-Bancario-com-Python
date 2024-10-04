menu = '''
Digite a opção desejada:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saque = 0
LIMITE_QUANTIDADE_SAQUE = 3

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        print('Depósito')
        valor_deposito = int(input('Selecione o valor do depósito: R$ '))
        saldo += valor_deposito
        print(f'Você depositou o valor de R$ {valor_deposito:.2f}')
        extrato += f'Depósito valor R$ {valor_deposito:.2f}\n'

    elif opcao == 's':
        print('Sacar')
        valor_do_saque = float(input('Digite o valor do saque: R$ '))

        exceder_saldo = valor_do_saque > saldo

        exceder_limite_unt = valor_do_saque > limite_valor_saque

        exceder_quant_max_saque = numero_saque >= LIMITE_QUANTIDADE_SAQUE

        if exceder_saldo:
            print('Operação falhou. Saldo insuficiente')
        
        if exceder_limite_unt:
            print('Operação falhou. Limite máximo por saque atingido')

        if exceder_quant_max_saque:
            print('Operação falhou. Limite máximo diário atingido.')

        elif valor_do_saque > 0:
            saldo -= valor_do_saque
            numero_saque += 1
            extrato += f'Saque valor R$ {valor_do_saque :.2f}\n'

        else:
            print('Número digitado é inválido')
  



    elif opcao == 'e':
        print('\n=========== Extrato ===========')
        if extrato > "":
            print(extrato)
        else:
            print('Não foram realizadas movimentações')
        
        print(f'\nSaldo bancário: R$ {saldo:.2f}')
        print('===================================')


    elif opcao == 'q':
        print('Obrigado pela preferência, volte sempre')

        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')