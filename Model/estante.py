class Estante:
    def __init__(self, codigo, disponibilidade):
        self.codigo = codigo
        self.disponibilidade = disponibilidade

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_disponibilidade(self):
        return self.disponibilidade

    def set_disponibilidade(self, n):
        self.disponibilidade = n
