# métodos de classe + factories

class Pessoa:
    ano = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("Hey")

    @classmethod
    def criar_com_50(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anonima', idade)



p1 = Pessoa('João',34)
Pessoa.metodo_de_classe()
p2 = Pessoa.criar_com_50('Helena')
p3 = Pessoa.criar_sem_nome(25)

print(p2.nome, p2.idade)
print(p3.nome, p3.idade)