class Secao:
    def __init__(self, codigo=None, numero_gavetas=0):
        self.codigo = codigo
        self.numero_gavetas = numero_gavetas

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_numero_gavetas(self):
        return self.numero_gavetas

    def set_numero_gavetas(self, numero_gavetas):
        self.numero_gavetas = numero_gavetas
