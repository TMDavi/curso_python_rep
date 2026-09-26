# @property - um getter no modo pythonico
# getter - um metodo para obter um atributo
# COdigo cliente é o codigo que usa o seu codigo


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 12234


c1 = Caneta('Azul')
print(c1.cor_tinta)






# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor

#     def get_cor(self):
#         print("Get cor")
#         return self.cor

    

    