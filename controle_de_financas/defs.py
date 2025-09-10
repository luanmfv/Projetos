def adicionar_despesa(despesas):
    nome = input("Digite o nome da despesa: ")
    valor = float(input("Digite o valor da despesa: R$"))
    despesa = {"nome": nome, "valor": valor}
    despesas.append(despesa)
    print("Despesa adicionada com sucesso!")

def listar_despesas(despesas):
    if not despesas:
        print("Não há despesas cadastradas.")
    else:
        print("Lista de despesas:")
        for despesa in despesas:
            print(f"Nome: {despesa['nome']}\nValor: R${despesa['valor']:.2f}\n")
