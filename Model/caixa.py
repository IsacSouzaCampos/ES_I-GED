import os


class Caixa:
    def __init__(self, codigo, estante):
        self.codigo = codigo
        self.estante = estante

    def get_estante(self):
        return self.estante

    def set_estante(self, estante):
        self.estante = estante

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
