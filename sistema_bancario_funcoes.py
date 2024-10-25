from datetime import date, datetime
mascara_ptbr = '%d/%m/%Y %H:%M:%S %a'
data_hora = datetime.now()
#melhorando o sistema antigo utilizando funções
def menu():
    menu = '''
    ===Bem vindo ao Banco do Sacrifício===
    [d]Depósito
    [s]Saque
    [e]Extrato
    [nu]Novo usuário
    [nc]Nova conta
    [lc]Listar contas
    [q]sair
    =>'''
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        data_hora = datetime.now()
        extrato += f'\nDepósito R$ {valor:.2f} realizado com sucesso! '
        extrato += f'Data da transação {data_hora.strftime(mascara_ptbr)}'
        print(f'Depósito no valor de R$ {valor:.2f} realizado com sucesso')
    else:
        print('@@ Valor informado é invalido @@')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('Operação falhou! Saldo insuficiente')
    
    elif excedeu_limite:
        print('Operação falhou! Limite saque atingido')

    elif excedeu_saques:
        print('Operação falhou! Limite de saques diários atingidos')
    
    elif valor > 0:
        saldo -= valor
        numero_saques +=1
        data_hora = datetime.now()
        extrato += f'\nSaque R$ {valor:.2f} realizado com sucesso! '
        extrato += f'Data da transação {data_hora.strftime(mascara_ptbr)}'
        print(f'Saque no valor de R$ {valor:.2f} realizado com sucesso')

    else:
        print('Operação falhou! Valor informado é inválido')


    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n===== EXTRATO =====')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo R$ {saldo:.2f}')
    print('=======================')

def criar_usuario(usuarios):
    cpf = input('Informe seu CPF (Somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nJá existe um usuário com este CPF!')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe sua data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe seu endereço (rua, nro, bairro, cidade/uf): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuário criado com sucesso')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nConta criada com sucesso')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\nUsuário não encontrado, criação de conta encerrado!')

def listar_contas(contas):
        if not contas:
            print('Nenhuma conta cadastrada.')
        else:
            for conta in contas:
                linha = f'''\
                    Agência:{conta['agencia']}\n
                    Conta corrente: {conta['numero_conta']}\n
                    Titular: {conta['usuario']['nome']}
                '''
                print(linha)
                print('=' * 100)
                
       

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    saldo = 500
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: R$ '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor do saque: R$ '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)


        elif opcao == 'q':
            break

        else:
            print('Operação inválida, por favor seleciona a operação desejada')   

main()



   














