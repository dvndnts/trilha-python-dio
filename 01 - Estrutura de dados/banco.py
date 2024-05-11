def deposito():
    global saldo
    valor_deposito = float(input("Digite o valor que deseja depositar: "))
    if valor_deposito < 0:
        print("Não é possível fazer depósito de valor negativo.")
        return None, saldo
    else:
        saldo += valor_deposito
        return f'Deposito: R$ {valor_deposito:.2f} \n', saldo


def saque(saldo, limite):
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque > saldo:
        print("Não será possível sacar o dinheiro por falta de saldo")
        return None, saldo
    elif valor_saque > limite:
        print(f'\nValor máximo de saque: R$ {limite}')
        return None, saldo
    elif valor_saque < 0:
        print("Não é possível fazer saque de valor negativo.")
        return None, saldo
    else:
        saldo -= valor_saque
        return f'Saque: R$ {valor_saque:.2f}\n', saldo


def gerar_extrato(extrato, saldo):
    print(' Extrato '.center(50, '#'))
    print(extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('#'.center(50, '#'))


saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


print(' Menu '.center(50, "#"))
while True:
    opcao = int(input(
        """ 
Olá! Ficamos felizes em te ter como cliente. O que você gostaria de fazer hoje?
    [1] Fazer Depósito
    [2] Fazer Saque
    [3] Ver Extrato
    [4] Sair
                         """))

    if opcao == 1:
        atualizacao_extrato, saldo = deposito()
        if atualizacao_extrato is not None:
            extrato += atualizacao_extrato
        # print(extrato)

    elif opcao == 2:
        if numero_saques >= LIMITE_SAQUES:
            print('Máximo de saques atingido')
        else:
            atualizacao_extrato, saldo = saque(saldo, limite)
            if atualizacao_extrato is not None:
                extrato += atualizacao_extrato
                numero_saques += 1
                # print(extrato)
    elif opcao == 3:
        gerar_extrato(extrato, saldo)
    elif opcao == 4:
        break
    else:
        print("Opção inválida!")
