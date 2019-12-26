

class PalavraSecreta():

    def __init__(self, palavra_secreta: str):
        self._palavra_secreta = palavra_secreta.upper()
        self._palavra_descoberta = "_" * len(palavra_secreta)

    @property
    def palavra_secreta(self):
        return self._palavra_secreta

    @property
    def palavra_descoberta(self):
        return self._palavra_descoberta

    @palavra_descoberta.setter
    def palavra_descoberta(self, palavra_descoberta):
        self._palavra_descoberta = palavra_descoberta

    def tem_letra(self, letra: str):
        return True if letra.upper() in self.palavra_secreta else False

    def substitui_letra_na_palavra(self, letra_tentativa: str):
        letra_tentativa = letra_tentativa.upper()

        for i in range(len(self.palavra_secreta)):
            if letra_tentativa == self.palavra_secreta[i]:
                self.palavra_descoberta = self.palavra_descoberta[:i] + letra_tentativa + self.palavra_descoberta[i+1:]
