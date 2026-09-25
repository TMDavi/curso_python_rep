class Pessoa:
    ANO_ATUAL = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ANO_ATUAL - self.idade

p1 = Pessoa('Joao', 35)
p2 = Pessoa('Helena',12)

print(Pessoa.ANO_ATUAL)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())