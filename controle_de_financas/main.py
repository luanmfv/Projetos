import menu
import defs
from time import sleep
despesas = []


mensagem = "Bem vindo ao sistema de controle de finanças"
cabecalho = "-" * 50
print(cabecalho)
print(mensagem.center(50))
print(cabecalho)

sleep(1.5)
salario = float(input("Digite o seu salário: R$"))
sleep(1.5)
print(" ")
print("Salário registrado com sucesso")
print(" ")
sleep(1.5)

while True:
    sleep(1.5)
    menu.m()
    print(" ")
    opcao = int(input("Digite uma opção: "))
    sleep(1.5)
    if opcao == 1:
        defs.adicionar_despesa(despesas)
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
    elif opcao == 3:
        print(' ')
        defs.listar_despesas(despesas)
        continue
    elif opcao == 4:
        print(f"Seu salário é: R${salario:.2f}")
    elif opcao == 5:
        total_despesas = sum(despesa['valor'] for despesa in despesas)
        saldo_restante = salario - total_despesas
        print(f"Seu saldo restante é: R${saldo_restante:.2f}")
    elif opcao == 6:
        print("Saindo do sistema...")
        sleep(1.5)
        break
            
            

