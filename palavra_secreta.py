import random

banco_palavras = [ # Aqui colocamos as palavras para o programa escolher
    'casa', 'gato', 'cachorro', 'computador', 'python', 'programa', 
    'jogo', 'adivinhacao', 'palavra', 'letra', 'teclado', 'tela',
    'musica', 'livro', 'caneta', 'caderno', 'escola', 'estudo',
    'trabalho', 'amigo', 'familia', 'comida', 'agua', 'fogo',
    'terra', 'ar', 'vento', 'chuva', 'sol', 'lua', 'estrela',
    'planeta', 'pais', 'cidade', 'rua', 'carro', 'onibus', 'bicicleta',
    'aviao', 'navio', 'hotel', 'praia', 'montanha', 'floresta', 'rio',
    'mar', 'peixe', 'passaro', 'flor', 'arvore', 'fruta', 'verdura',
    'legume', 'tempo', 'relogio', 'calendario', 'numero', 'letra',
    'cor', 'forma', 'tamanho', 'sabor', 'cheiro', 'som', 'voz',
    'olho', 'ouvido', 'nariz', 'boca', 'mao', 'pe', 'braco', 'perna',
    'coracao', 'mente', 'ideia', 'pensamento', 'sonho', 'vida', 'doutor', 'mundo'
]

palavra = random.choice(banco_palavras) # Aqui o programa escolhe uma palavra do banco de palavras
palavra_adivinhada = ['_'] * len(palavra) # Aqui o programa substitui todas as letras da palavra escolhida por '_'

tentativas = 10

print('Jogo da Palavra secreta!')
print('Adivinhe a palavra.')

while tentativas > 0:
    print('\nPalavra atual: ' + ' '.join(palavra_adivinhada)) # Aqui o programa exibe a quantidade de '_' que corresponde à quantidade de letras da palavra escolhida
    adivinha = input('Adivinhe uma letra: ').lower() # O usuário nessa parte pode colocar uma letra que ele acredita ser da palavra escolhida

    if adivinha in palavra: # Nessa seção o programa verifica se a letra digitada está entre a palavra e informa o usuário, além de exibir a posição da letra
        for i in range(len(palavra)):
            if palavra[i] == adivinha:
                palavra_adivinhada[i] = adivinha
        print('Boa adivinhação!')
    else: # Se a letra digitada não estiver na palavra, o programa informa o usuário e informa a quantidade de tentativas atual
        tentativas -= 1
        print('Letra errada! Tentativas restantes: ' + str(tentativas))
    
    if '_' not in palavra_adivinhada: # Quando não há mais '_' na palavra escolhida pelo programa, significa que o usuário venceu, e o programa exibe isso
        print('\nParabéns! Você adivinhou a palavra: ' + palavra) 
        break

if tentativas == 0 and '_' in palavra_adivinhada: # Se acabam as tentativas do usuário e ele não acertou, o programa exibe a mensagem informando que ele perdeu, e qual era a palavra
    print('\nVocê não tem mais tentativas. A palavra era: ' + palavra)
