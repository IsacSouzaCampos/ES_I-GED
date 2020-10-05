import os


class Estante:
    def __init__(self, codigo=None):
        self.codigo = codigo

    @staticmethod
    def existe_estante(codigo):
        return os.path.exists(f'data/arquivo/{codigo}')

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
