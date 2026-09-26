# method vs @classmethod vs @staticmethod
# - como getter
# p/ evitar quebrar código cliente
# p/ habilitar setter
# p/ executar ações ao obter um atributo
# Atributos que começam com um ou dois underlines
# nao devem ser usados fora da classe

class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor

caneta = Caneta('Azul')
# caneta.cor = 'Rosa'

# print(caneta.cor)


    