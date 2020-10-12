import os


class Caixa:
    def __init__(self, estante, codigo):
        self.estante = estante
        self.codigo = codigo

    def verificar_existencia(self):
        os.path.exists(f'data/arquivo/{self.get_estante()}/{self.get_codigo()}')

    def adicionar(self):
        os.system(f'touch data/arquivo/{self.get_estante()}/{self.get_codigo()}')

    def get_estante(self):
        return self.estante

    def set_estante(self, estante):
        self.estante = estante

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
