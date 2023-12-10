menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastro
[cl] Clientes
[nc] Nova Conta
[co] Contas
[q] Sair

'''


def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato.append(f'Depósito: + {valor_deposito:.2f}')
        print('Depósito realizado com sucesso!')
    else:
        print('Por favor, insira um valor de depósito válido (positivo)!')
    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite, LIMITE_SAQUES):
    global numero_saques
    if numero_saques < LIMITE_SAQUES:
        if valor_saque > 0:
            if 500 >= valor_saque <= saldo:
                saldo -= valor_saque
                extrato.append(f'Saque: - {valor_saque:.2f}')
                print('Saque realizado com sucesso!')
                numero_saques += 1
            elif valor_saque > saldo:
                print('Saldo insuficiente!')
            else:
                print('Valor maior do que o limite permitido!')
        else:
            print('Por favor, insira um valor de saque válido (positivo)!')
    else:
        print('Limite de saque diario excedido!')
    return saldo, extrato

def pedir_extrato(saldo, /, *, extrato):
    for operacao in extrato:
        print(operacao)
    print(f'\nExtrato: {saldo:.2f}')
    return saldo, extrato

def cadastro_clente():
    cpf = int(input('Digite seu CPF (apenas números): '))
    for cliente in lista_cliente:
        if cliente['CPF'] == cpf:
            print('CPF já cadastrado. Tente novamente!')
            return
    nome = input('Digite seu nome: ')
    data_nascimento = input('Digite sua data de nascimento (dd/mm/aa): ')
    endereco = input('Digite seu endereço (Logradouto, N° - Bairro - Cidade/Sigla Estado): ')

    lista_cliente.append({'Nome': nome, 'CPF': cpf, 'Data de Nascimento': data_nascimento, 'Endereço': endereco})
    print('Cadastro realizado com sucesso!')

def criar_conta(agencia, lista_cliente):
    global numero_conta
    cpf_cliente = int(input('Informe o CPF do cliente (Apenas números): '))
    for cliente in lista_cliente:
        if cliente['CPF'] == cpf_cliente:
            contas.append({'Agência': agencia, 'Número da Conta': numero_conta, 'Cliente': cliente['Nome']})
            print('Conta criada com sucesso!')
            numero_conta += 1
            return
    print('Cliente não encontrado!')

saldo = 0
limite = 500
extrato = []
lista_cliente = []
contas = []
numero_conta = 1
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        valor_deposito = float(input('Quando deseja depositar? '))
        saldo, extrato = depositar(saldo, valor_deposito, extrato)
    
    elif opcao == 's':
        valor_saque = float(input('Quanto deseja sacar? '))
        saldo, extrato = sacar(
            saldo=saldo,
            valor_saque=valor_saque,
            extrato=extrato,
            limite=limite,
            LIMITE_SAQUES=LIMITE_SAQUES,
        )
    
    elif opcao == 'e':
        pedir_extrato(saldo, extrato=extrato)

    elif opcao == 'c':
        cadastro_clente()
    
    elif opcao == 'cl':
        print('----- LISTA DE CLIENTES -----\n')
        for cliente in lista_cliente:
            print(f"Nome: {cliente['Nome']}\nCPF: {cliente['CPF']}\nData de Nascimento: {cliente['Data de Nascimento']}\nEndereço: {cliente['Endereço']}\n")
            
    elif opcao == 'nc':
        criar_conta(AGENCIA, lista_cliente)

    elif opcao == 'co':
        for conta in contas:
            print(f"Agência: {conta['Agência']}\nConta: {conta['Número da Conta']}\nCliente: {conta['Cliente']}\n")

    elif opcao == 'q':
        print('Operação finalizada!')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')