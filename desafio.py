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
LIMITES_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor de deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
            print("Deposito realizado com sucesso!")

        else:
            print("Opção falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saque = numero_saques >= LIMITES_SAQUES
                
        if excedeu_saldo:
                print("Operação inválida! Saldo insuficiente.")
        
        elif excedeu_limite:
                print("Operação inválida! limite excedido.")
            
        elif excedeu_saque:
                print("Operação inválida! Número máximo de saques excedido.")
                
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
            print("Saque realizado com sucesso!")
        
        else:
            print("Operação falhou! O valor informado é inválido.")
            
    elif opcao == "3":
        print("\n ============== EXTRATO ==============")
        print("Não foram realizadas movimentações em sua conta" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================")
        
    elif opcao == "0":
        break
    
    else:
        print("Opreação inválida, por favor selecione novamente a operação desejada") 