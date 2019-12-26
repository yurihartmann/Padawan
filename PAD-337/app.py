import random
import functions

cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']

cartas_jogador = []
soma_jogador = 0

# embaralhando as cartas
print("Embaralhando as cartas...")
random.shuffle(cartas)

continuar = True

while continuar:
    carta = cartas.pop(0)

    print(f'\nCarta sorteado foi: "{carta}"!!!')

    valor_carta = functions.convert_carta_in_value(carta)

    if len(cartas_jogador) == 0 and carta == 'A':
        valor_carta = 11

    cartas_jogador.append(carta)
    soma_jogador += valor_carta

    print(f"Suas cartas são {cartas_jogador}")
    print(f"Soma das cartas é: {soma_jogador}")

    if len(cartas) == 0 or soma_jogador >= 21:
        break
    else:
        continuar = functions.quer_continuar()

print('Fechando programa...')