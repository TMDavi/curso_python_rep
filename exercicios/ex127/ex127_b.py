import json

class Curso:

    def __init__(self, nome, n_aulas, carga_horaria):

        self.nome = nome
        self.n_aulas = n_aulas
        self.carga_horaria = carga_horaria

    def devolve_dict(self):
        return self.__dict__

with open('classe.json','r') as file:
    dados = json.load(file)

curso1 = Curso(**dados)
print(curso1.__dict__)