class Pessoa:
    ANO_ATUAL = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ANO_ATUAL - self.idade

p1 = Pessoa('Joao', 35)
p1.__dict__['nome'] = 'EITA'
p1.__dict__['outra'] = 'coisa'
del p1.__dict__['nome']

print(p1.__dict__)
print(vars(p1))