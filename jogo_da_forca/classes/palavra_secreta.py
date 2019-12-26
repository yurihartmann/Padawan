

class PalavraSecreta():

    def __init__(self, palavra_secreta: str):
        self.__palavra_secreta = palavra_secreta.upper()
        self.__palavra_descoberta = "_" * len(palavra_secreta)

    @property
    def palavra_secreta(self):
        return self.__palavra_secreta

    @property
    def palavra_descoberta(self):
        return self.__palavra_descoberta


    def verificacao_letra(self, letra_tentativa: str):
        tem_letra = False
        letra_tentativa = letra_tentativa.upper()

        for i in range(len(self.__palavra_secreta)):
            if letra_tentativa == self.__palavra_secreta[i]:
                self.__palavra_descoberta = self.__palavra_descoberta[:i] + letra_tentativa + self.__palavra_descoberta[i+1:]
                tem_letra = True

        return tem_letra

    def ganhou(self):
        return True if '_' not in self.palavra_descoberta else False
