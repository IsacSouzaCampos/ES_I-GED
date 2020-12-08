class Estante:
    def __init__(self, codigo, disponibilidade, caixas=None):
        self.codigo = codigo
        self.disponibilidade = disponibilidade
        self.caixas = caixas

    def adicionar_caixa(self, caixa):
        self.caixas.append(caixa)

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_disponibilidade(self):
        return self.disponibilidade

    def set_disponibilidade(self, n):
        self.disponibilidade = n

    def get_caixas(self):
        return self.caixas

    def set_caixas(self, caixas):
        self.caixas = caixas
