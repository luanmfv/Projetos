def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mErro, digite um numero inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[0;31mUsuario preferiu não digitar esse número.\033[m')  # \n é para quebrar a linha e mostrar abaixo
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42)) #para ficar no centro de 42 linhas
    print(linha())


def menu(lista):
    cabeçalho('MENU')
    c = 1
    for item in lista:
        print(f'\033[35m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc



