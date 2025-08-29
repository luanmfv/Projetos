import menu
despesas = []

mensagem = "Bem vindo ao sistema de controle de finanças"
print("-" * len(mensagem))
print(mensagem)
print("-" * len(mensagem))

salario = float(input('Digite o seu salário:R$'))
print (f'Seu salário é:R${salario:.2f}')
menu.m()

opcao = int(input("Digite uma opção: "))
if opcao == 1:
    nome = str(input("Digite o nome da despesa: "))
    valor = float(input("Digite o valor da despesa: R$"))
    despesa = {"nome": nome, "valor": valor}
    despesas.append(despesa)
    print(despesas)
else:
    print("Você escolheu")


"""
    print('1 - Adicionar despesa')
    print('2 - Remover despesa')
    print('3 - Listar despesas')
    print('4 - Sair')
"""
            

