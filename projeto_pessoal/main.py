import menu
despesas = []

menu.m()
while True:
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        nome = str(input("Digite o nome da despesa: "))
        valor = float(input("Digite o valor da despesa: R$"))
        despesa = {"nome": nome,"valor": valor}
        despesas.append(despesa)
        for despesa in despesas:
            print(f"Nome: {despesa['nome']}\nValor: R${despesa['valor']:.2f}\n")
        print("-" * len("Despesa adicionada com sucesso!"))
        print("Despesa adicionada com sucesso!")
        print("-" * len("Despesa adicionada com sucesso!"))
    elif opcao == 2:
        print("Qual despesa deseja remover?")
        print(despesas)
        escolha = str(input("Digite o nome da despesa (z para voltar): "))
        if escolha == "z":
            continue
        else:
            for despesa in despesas:
                if despesa["nome"] == escolha:
                    despesas.remove(despesa)
                    print("Despesa removida com sucesso!")
            else:
                print("Despesa não encontrada!")
                escolha = str(input("Digite o nome da despesa (z para voltar): "))
                if escolha == "z":
                    continue
            
                
            
                
            
                
            
                
                
            
            
            


"""
    print('1 - Adicionar despesa')
    print('2 - Remover despesa')
    print('3 - Listar despesas')
    print('4 - Sair')
"""
            

