import random
from blackjack.classes.blackjack import BlackJack
from blackjack.functions import quer_continuar

black_jack = BlackJack()

continuar = True

while continuar:
    carta = black_jack.pegar_carta()

    print(f'\nCarta sorteado foi: "{carta}"!!!')

    print(f"Suas cartas são {black_jack.cartas_jogador}")
    print(f"Soma das cartas é: {black_jack.soma_jogador}")

    if black_jack.alcancou_21():
        break
    else:
        continuar = quer_continuar()

print(f"Voce finalizou com {black_jack.soma_jogador} pontos !!!")
print('Fechando programa...')