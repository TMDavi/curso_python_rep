# Exercicio - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instancias
# da classe com os dados salvos
# Faça em arquivos separados

import json

class Curso:

    def __init__(self, nome, n_aulas, carga_horaria):

        self.nome = nome
        self.n_aulas = n_aulas
        self.carga_horaria = carga_horaria

    def devolve_dict(self):
        return self.__dict__

curso1 = Curso("Matematica", 30, 50)
dados = curso1.devolve_dict()

with open("classe.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    