from .. interface import cabeçalho

#parece que os dois pontos servem para importar algo da pasta irmão e da certo

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #open é um comando que abre o arquivo, e a sigla rt é read and text
        a.close() #close é para fechar o arquivo
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # write text e o + é para caso não exista arquivo ele cria
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';') #split separa os dados
            dado[1] = dado[1].replace('\n', '') #replace para repor a quebra de linha por nada
            print(f'{dado[0]:<30}{dado[1]:>3} anos')  #<30 alinhado a esquerda e dado 1 >3 alinhado a direita
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')  #append e texto, criar arquivo de texto
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
