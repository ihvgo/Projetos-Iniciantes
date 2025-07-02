import random
n = random.randint(0, 5) #Faz o computador "Pensar" em um número
escolha = int(input('Estou pensando em um número entre 0 e 5. Tente acertar qual número é: '))
if escolha == n:
    print('Você acertou o número que eu pensei.')
else:
    print('Você errou o número que eu pensei.')
