import random
from jogo_da_forca.classes.palavra_secreta import PalavraSecreta


class Forca:

    _PALAVRAS = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']
    __vidas = 8

    def __init__(self):
        self.__palavra = PalavraSecreta(random.choice(self._PALAVRAS))

    def iniciar(self):
        while not self.__palavra.ganhou():
            print(format(' Jogo da forca ', '=^50'))
            print("Palavra Secreta: " + self.__palavra.palavra_descoberta)
            print(f"Voce tem {self.__vidas} vida(s)..")
            self.chutar_letra()

            if self.__vidas == 0:
                print('Voce perdeu, suas vidas acabaram...')
                break

        if self.__palavra.ganhou():
            print('Parabens voce ganhou!!!')

    @property
    def vidas(self):
        return self.__vidas

    def chutar_letra(self):
        letra = self.get_uma_letra()
        tem_letra = self.__palavra.verificacao_letra(letra)
        if not tem_letra:
            self.__vidas -= 1

    def get_uma_letra(self):
        while True:
            letra = input("Digite uma letra: ")
            if len(letra) == 1 and letra.isalpha():
                return letra
            else:
                print('Digite apenas uma letra!!')

