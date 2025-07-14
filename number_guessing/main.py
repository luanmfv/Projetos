from random import randint

print('-' * 30)
print('Bem-vindo ao jogo de adivinhação de números!')
print('-' * 30)
a = int(input('Advinhe o número de 0 a 10:'))
b = randint(0, 10)
while a != b:
    if a < b:
        print('-' * 30)
        print('O número é maior que {}'.format(a))
        print('-' * 30)
    else:
        print('-' * 30)
        print('O número é menor que {}'.format(a))
        print('-' * 30)
    a = int(input('Tente novamente: '))
print('-' * 30)
print('Parabéns! Você acertou o número {}'.format(b))
print('-' * 30)
print('Fim do jogo!')
print('-' * 30)
