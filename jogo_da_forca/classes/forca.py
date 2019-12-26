import random
from jogo_da_forca.classes.palavra_secreta import PalavraSecreta


class Forca:
    _PALAVRAS = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']
    _vidas = 8
    _letra_escolida = ' '

    def __init__(self):
        self._palavra = PalavraSecreta(random.choice(self._PALAVRAS))

    @property
    def palavra(self):
        return self._palavra

    def iniciar(self):
        print(format(' Jogo da forca ', '=^50'))

        while not self.ganhou() and self.tem_vida():
            self.print_dados()
            self.pega_letra_escolida_pelo_jogador()

            if self.palavra.tem_letra(self._letra_escolida):
                self.palavra.substitui_letra_na_palavra(self._letra_escolida)
            else:
                self.perde_uma_vida()

        self.fim_de_jogo()

    def print_dados(self):
        print("Palavra Secreta: " + self.palavra.palavra_descoberta)
        print(f"Voce tem {self._vidas} vida(s)..")

    def pega_letra_escolida_pelo_jogador(self):
        while True:
            letra = input("Digite uma letra: ")
            if len(letra) == 1 and letra.isalpha():
                self._letra_escolida = letra
                break
            else:
                print('Digite apenas uma letra!!')

    def perde_uma_vida(self):
        self._vidas -= 1

    def tem_vida(self):
        return True if self._vidas > 0 else False

    def ganhou(self):
        return True if '_' not in self.palavra.palavra_descoberta else False

    def fim_de_jogo(self):
        if not self.tem_vida():
            print('Voce Perdeu')
            print('Acabou suas vidas..')
        else:
            print('Voce ganhou, parabens !!!')
