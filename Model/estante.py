import os


class Estante:
    def __init__(self, codigo, disponibilidade):
        self.codigo = codigo
        self.disponibilidade = disponibilidade

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
