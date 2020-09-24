class Usuario:
    def __init__(self, nome=None, numero_identificacao=None):
        self.nome = nome
        self.numero_identificacao = numero_identificacao

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_numero_identificacao(self):
        return self.numero_identificacao

    def set_numero_identificacao(self, numero_identificacao):
        self.numero_identificacao = numero_identificacao
