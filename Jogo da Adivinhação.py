import random
n = random.randint(0, 5) # Faz o computador "Pensar" em um número
escolha = int(input('Estou pensando em um número entre 0 e 5. Tente acertar qual número é: ')) # O jogador tenta adivinhar
if escolha == n:
    print('Você acertou o número que eu pensei.')
else:
    print(f'Você errou. O número que eu pensei foi {n}.')
