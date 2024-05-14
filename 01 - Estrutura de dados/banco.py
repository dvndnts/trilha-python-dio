import textwrap


def menu():

    print(' Menu '.center(50, "#"))
    menu = """
Olá! Ficamos felizes em te ter como cliente. O que você gostaria de fazer hoje?
    [1] Fazer Depósito
    [2] Fazer Saque
    [3] Ver Extrato
    [4] Ainda não é cliente e deseja fazer seu cadastro?
    [5] Fazer nova conta
    [6] Listar contas
    [7] Sair
                            """

    return input(menu)


def depositar(saldo, extrato, /):
    valor_deposito = float(input("Digite o valor que deseja depositar: "))
    if valor_deposito < 0:
        print("Erro: O valor informado é inválido: Valor negativo.")
        return None, saldo
    else:
        saldo += valor_deposito
        extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
        print('Depósito feito com sucesso!\n')
        return saldo, extrato


def saque(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saques_diarios = numero_saques >= LIMITE_SAQUES
    if excedeu_saques_diarios:
        print('\nErro: Número de saques diários foi excedido.\n')
        return saldo, extrato, numero_saques
    else:
        valor_saque = float(input("\nDigite o valor do saque: \n"))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        valor_saque_negativo = valor_saque < 0

        if excedeu_saldo:
            print("\nErro: Não há saldo suficiente para retirada deste valor :/ \n")
            return saldo, extrato, numero_saques
        elif excedeu_limite:
            print(f'\nErro: Valor máximo de saque: R$ {limite}\n')
            return saldo, extrato, numero_saques
        elif valor_saque_negativo:
            print("\nErro: Não é possível fazer saque de valor negativo.\n")
            return saldo, extrato, numero_saques
        else:
            saldo -= valor_saque
            extrato += f'Saque: R$ {valor_saque:.2f}\n'
            numero_saques += 1
            print('\nSaque feito com sucesso!\n')
            return saldo, extrato, numero_saques


def gerar_extrato(saldo, /, *, extrato):
    print(' Extrato '.center(50, '#'))
    if extrato:
        print(extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('#'.center(50, '#'))
        print()
    else:
        print('\nNão foram realizadas movimentações.\n')


def criar_usuario(usuarios):
    cpf, cpf_valido = filtrar_usuario(usuarios)
    if any(usuario.get('cpf') == int(cpf) for usuario in usuarios):
        print('\nErro: Já existe usuário com este CPF\n')
        # print('\nErro: CPF inválido. Tente novamente.\n')
        return usuarios  # Retorna a lista de usuários existentes, sem adicionar um novo
    else:
        nome = input('Digite o nome: ')
        data_de_nasc = input('Digite a data de nascimento (dd-mm-aaaa): ')

        logradouro, num_endereco = input("""Agora o endereço :D 
Qual seria a rua? """), input('Digite o número da casa: ')
        bairro = input('Qual o bairro? ')
        cidade = input('Qual a cidade? ')
        sigla_estado = input('Qual o estado (em sigla?) ')

        endereco = f'{logradouro}, {
            num_endereco} - {bairro}, {cidade}/{sigla_estado}'

        info_usuario = {'cpf': int(cpf), "name": nome,
                        "data_de_nasc": data_de_nasc, 'endereco': endereco, 'contas': []}

        usuarios.append(info_usuario)
        print('\nUsuário criado com sucesso. Ficamos felizes em te ter como cliente :)\n')

        return usuarios


def filtrar_usuario(usuarios):
    cpf = input('Digite o CPF: ')
    cpf_sem_simbolos = ''.join(i for i in cpf if i.isdigit())
    if len(cpf_sem_simbolos) == 11:
        return cpf_sem_simbolos, True
        # Verifica se o CPF já está registrado
        # return cpf_sem_simbolos, False
    # else:
    #         return cpf_sem_simbolos, True
    else:
        print('\nErro: CPF inválido. Tente novamente.\n')
        return None, False


def criar_conta(AGENCIA, num_contas, usuarios):
    cpf, cpf_valido = filtrar_usuario(usuarios)
    if cpf_valido:
        # Encontra o usuário pelo CPF
        for usuario in usuarios:
            if usuario.get('cpf') == int(cpf):
                num_contas += 1
                usuario["contas"].append(num_contas)
                print('\nConta cadastrada com sucesso!\n')
                # Retorna a conta com o nome do usuário
                return {"agencia": AGENCIA, 'num_contas': num_contas, 'usuarios': {'cpf': cpf, 'nome': usuario['name']}}
        else:
            print('Erro: CPF não encontrado em nossa base. Tente novamente.')
    else:
        print('\nErro: CPF inválido. Tente novamente.\n')
        return None


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['num_contas']}
            Titular:\t{conta['usuarios']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    # constantes
    AGENCIA = '0001'
    LIMITE_SAQUES = 3

# Criação de usuário e conta
    usuarios = []
    contas = []
    num_contas = 0

    # Operacoes
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0

    while True:
        opcao = menu()

        if opcao == '1':
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == '2':
            saldo, extrato, numero_saques = saque(saldo=saldo, extrato=extrato, limite=limite,
                                                  numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
        elif opcao == '3':
            gerar_extrato(saldo, extrato=extrato)
        elif opcao == '4':
            usuarios = criar_usuario(usuarios)
        elif opcao == '5':
            criando_conta_bancaria = criar_conta(AGENCIA, num_contas, usuarios)
            if criando_conta_bancaria is not None:
                contas.append(criando_conta_bancaria)
                num_contas += 1
        elif opcao == '6':
            listar_contas(contas)
        elif opcao == '7':
            break
        else:
            print("Opção inválida!")


main()
