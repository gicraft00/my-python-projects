import random

def jogar():
    """ Função principal do jogo pedra, papel e tesoura """
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.choice(opcoes)

    jogador = input('escolha entre pedra, papel ou tesoura:')

    if jogador not in opcoes:
        print('Opção inválida. Tente novamente.')
        return
    print(f'Computador escolheu: {computador}')
    if jogador == computador:
        print('Empate!')
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        print('Você venceu!')
    else:
        print('Você perdeu!')

if __name__ == '__main__':
    jogar()