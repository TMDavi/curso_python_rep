# Encapsulamento (Modificadores de acesso:: publica, protected, private)
# Python nao tem omodificadores de acesso
# Mas podemos seguir as seguintes convenções
#     (sem underline) = public
        # pode ser usado em qualquer lugar
#     (um underline) = protected
        # nao deve ser usado fora da classe
        # ou subclasses
#     (dois underline) = private
        # só deve ser usado na classe que foi declarado

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
    
    def metodo_publico(self):
        return 'metodo publico'


f = Foo()

print(f.public)
print(f.metodo_publico())