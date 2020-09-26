class Estante:
    def __init__(self, codigo=None):
        self.codigo = codigo

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
