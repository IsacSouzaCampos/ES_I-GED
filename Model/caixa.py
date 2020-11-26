import os


class Caixa:
    def __init__(self, codigo, codigo_estante):
        self.codigo = codigo
        self.codigo_estante = codigo_estante

    def get_codigo_estante(self):
        return self.codigo_estante

    def set_codigo_estante(self, codigo_estante):
        self.codigo_estante = codigo_estante

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
