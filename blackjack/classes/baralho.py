import random


class Baralho:

    cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']

    def __init__(self):
        pass

    def embaralhar(self):
        random.shuffle(self.cartas)