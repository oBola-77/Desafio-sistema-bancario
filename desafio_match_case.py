menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    match opcao:

        case "1":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Deposito: R$ {valor:.2f}\n"

                print("Deposito realizado com sucesso!")

            else:
                print("Opção falhou! O valor informado é inválido.")

        case "2":
             valor = float(input("Informe o valor do saque: "))

             excedeu_saldo = valor > saldo
             
             excedeu_limite_saque = valor > limite

             excedeu_saque = numero_saques >= LIMITE_SAQUE

             if excedeu_saldo:
                 print("Operação incompleta! Saldo insuficiente.")

             elif excedeu_limite_saque:
                 print("Operação incompleta! Limite excedido.")

             elif excedeu_saque:
                print("Operação incompleta! Número máximo de saques excedido.")

             elif valor > 0:
                 saldo -= valor
                 extrato += f"Saque: R$ {valor:.2f}\n"
                 numero_saques += 1

                 print("Saque realizado com sucesso!")

             else:
                print("Operação falhou! O valor informado é inválido.")

        case "3":
            print("\n ============== EXTRATO ==============")
            print("Não foram realizados movimentações na sua conta. " if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("============================")

        case "0":
            break

        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada")