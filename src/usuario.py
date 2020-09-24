class Usuario:
    def __init__(self, nome=None):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
