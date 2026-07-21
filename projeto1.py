menu = """

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito R$: {valor:.2f}\n"

        else:
            print("Operacao falhou, O valor informado é invalido")


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_limite:
            print("Operacao falhou! O valor do saque excede o limite.")

        elif excedeu_saldo:
            print("Operacao falhou! Voce nao tem saldo suficiente para a operacao.")

        elif excedeu_saques:
            print("Operacao falhou! Numero maximo de saques excedidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$: {valor:.2f}\n"
            numero_saque += 1
        
        else:
            print("Operacao falhou! O valor informado e invalido.")



    elif opcao == "e":
        print("\n===================== EXTRATO =====================")
        print("Nao foram realizadas movimentacoes na conta" if not extrato else extrato)
        print(f"\nSaldo atual R$: {saldo:.2f}")
        print("=====================================================")


    elif opcao == "q":
        break


    else:
        print("Operacao Invalida! Por favor selecione novamente a opcao desejada.")