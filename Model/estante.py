import os


class Estante:
    def __init__(self, codigo=None):
        self.codigo = codigo

    def adicionar(self):
        try:
            if not self.existe_estante():
                os.system(f'mkdir data/arquivo/{self.get_codigo()}')
            else:
                raise Exception('Estante ja existente')
        except Exception as e:
            raise e

    def existe_estante(self):
        return os.path.exists(f'data/arquivo/{self.get_codigo()}')

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
