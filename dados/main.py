from random import randint
import menu
from time import sleep

print('Bem vindo ao sistema de dados!')
menu.menu_dados()
while True:
    a = randint(1, 6)
    b = int(input('Escolha uma opção: '))
    if b == 1:
        print('-' * 20)
        print('Jogando o dado...')
        sleep(2)
        print('')
        print(f'O dado caiu no número {a}')
        sleep(2)
        menu.menu_dados()
    elif b == 2:
        print('Saindo do jogo...')
    else:
        print('Opção inválida!')
    if b == 2:
        break
