menu = """

[d] DEPOSITAR
[s] SACAR
[e] EXTRATO
[q] SAIR


=> """

saldo = 0
limite = 500
extrato = ''
numeros_saques = 0
LIMITE_SAQUES = 3  # Define o limite de saques diários
LIMITE_SAQUE = 500  # Define o limite máximo por saque

while True:

    opcao = input(menu)  # Exibe o menu e aguarda a entrada do usuário

    if opcao == 'd':
        # Opção para depositar: solicita ao usuário o valor e adiciona ao saldo se for válido
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Por favor, digite um valor positivo.")

    elif opcao == 's':
        # Opção para sacar: verifica o limite de saques diários e a disponibilidade de saldo
        if numeros_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if valor_saque > 0 and valor_saque <= saldo and valor_saque <= LIMITE_SAQUE:
                saldo -= valor_saque
                numeros_saques += 1
                extrato += f"Saque de R${valor_saque:.2f}\n"  # Atualiza o extrato com o saque realizado
                print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
            else:
                print("Valor de saque inválido ou saldo insuficiente ou excedeu o limite máximo por saque.")
        else:
            print("Você atingiu o limite de saques diários.")

    elif opcao == 'e':
        # Opção para visualizar o extrato: mostra todos os saques realizados e o saldo atual
        print("########################## EXTRATO ##########################")
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}")
        print()
        print("#############################################################")

    elif opcao == 'q':
        # Opção para sair do programa: encerra o loop
        print("Saindo do programa.")
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada. ')
