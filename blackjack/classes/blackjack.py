from blackjack.classes.baralho import Baralho


class BlackJack(Baralho):

    soma_jogador = 0
    cartas_jogador = []

    def __init__(self):
        super().__init__()
        self.embaralhar()

    def pegar_carta(self):
        carta = self.cartas.pop(0)
        self.soma_jogador += self.valor_da_carta(carta)
        self.cartas_jogador.append(carta)
        return carta

    def valor_da_carta(self, carta):
        try:
            n = int(carta)
        except:
            if len(self.cartas_jogador) == 0 and carta == 'A':
                return 11
            elif carta == 'A':
                return 1
            elif carta in 'JQK':
                return 10
        else:
            return n

    def alcancou_21(self):
        return True if self.soma_jogador >= 21 else False
