from blackjack.classes.deck import Deck
from blackjack.classes.cards import Ace

class BlackJack(Deck):

    def __init__(self):
        super().__init__()
        self.shuffle_deck()
        self._points = 0
        self._player_cards = []

    def start(self):
        print(format(' BlackJack ', '=^50'))

        while not self.has_21_points() and self.want_to_continue():
            self.get_card_in_deck()
            self.calc_player_points()
            self.print_status_game()

        self.end_game()

    def print_status_game(self):
        print(f"Suas cartas são ", end='')
        for card in self._player_cards:
            print(f"{card} - ", end='')
        print()
        print(f"Soma das cartas é: {self._points}")

    def get_card_in_deck(self):
        card = self._cards.pop(0)
        self._player_cards.append(card)

    def calc_player_points(self):
        cont = 0
        for card in self._player_cards:
            if cont == 0 and card is Ace():
                cont += 11
            else:
                cont += card.get_value()

        self._points = cont

    def has_21_points(self):
        return True if self._points >= 21 else False

    def want_to_continue(self):
        while True:
            chosse = input('Quer pegar uma carta? (S/N) ').upper()
            if chosse == 'S':
                return True
            elif chosse == 'N':
                return False
            else:
                print('Opção inválida!')

    def end_game(self):
        print(f'Voce finalizou com {self._points} pontos !!!')


