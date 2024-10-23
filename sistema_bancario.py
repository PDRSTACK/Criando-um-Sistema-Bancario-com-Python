from datetime import date, datetime
data_hora = datetime.now()
mascara_ptbr = "%d/%m/%Y %H:%M:%S %a"

menu = '''
Digite a opção desejada:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saque = 0
LIMITE_QUANTIDADE_SAQUE = 3

while True:
    opcao = input(menu)
    
    if opcao == 'd': #Fazendo a função de depósito
        print('Depósito')
        valor_deposito = int(input('Selecione o valor do depósito: R$ ')) # recebendo valor depósito
        saldo += valor_deposito #adicionando valor depósito ao saldo
        print(f'Você depositou o valor de R$ {valor_deposito:.2f}') #confirmação de saldo
        extrato += f'Depósito valor R$ {valor_deposito:.2f}\n' #adicionando informação de depósito ao extrato
        data_hora = datetime.now()
        mascara_ptbr = "%d/%m/%Y %H:%M:%S %a"
        extrato += f'Data da transação {data_hora.strftime(mascara_ptbr)}\n'

    elif opcao == 's': #fazendo função saque
        print('Sacar')
        valor_do_saque = float(input('Digite o valor do saque: R$ ')) #recebendo o valor do saque

        exceder_saldo = valor_do_saque > saldo # Variável para controlar valor do saque está disponível

        exceder_limite_unt = valor_do_saque > limite_valor_saque # Variável para controlar limite de valor por saque

        exceder_quant_max_saque = numero_saque >= LIMITE_QUANTIDADE_SAQUE # variavel para controlar a quantidade máxima de saque

        if exceder_saldo: #condição para se o saque exceder o saldo 
            print('Operação falhou. Saldo insuficiente')
        
        elif exceder_limite_unt: #condição para se o saque exceder o limite unitário de valor
            print('Operação falhou. Limite máximo por saque atingido')

        elif exceder_quant_max_saque: #condição para se o saque atingir a quantidade máxima de saque diário
            print('Operação falhou. Limite máximo diário atingido.')

        elif valor_do_saque > 0: #condição para se o valor do saque for maior que 0 e não exceda nenhum limite
            saldo -= valor_do_saque # para subtrair o valor do saque do saldo
            numero_saque += 1 # contador para não exceder limite de saque diário
            extrato += f'Saque valor R$ {valor_do_saque :.2f}\n' #adicionando transação ao extrato
            data_hora = datetime.now()
            mascara_ptbr = "%d/%m/%Y %H:%M:%S %a"
            extrato += f'Data da transação {data_hora.strftime(mascara_ptbr)}\n'
        else:
            print('Número digitado é inválido')
  



    elif opcao == 'e': #condição para o extrato
        print('\n=========== Extrato ===========')
        if extrato > "":
            print(extrato)
        else:
            print('Não foram realizadas movimentações')
        
        print(f"\nSaldo: R$ {saldo:.2f}") #informando o saldo
        print('===================================')


    elif opcao == 'q': #condição para sair do sistema
        print('Obrigado pela preferência, volte sempre')

        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')