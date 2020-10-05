import os


class Caixa:
    def __init__(self, estante, codigo):
        self.estante = estante
        self.codigo = codigo

    def verificar_existencia(self):
        os.path.exists(f'data/arquivo/{self.estante}/{self.codigo}')

    def adicionar(self):
        os.system(f'touch data/arquivo/{self.estante}/{self.codigo}')

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
