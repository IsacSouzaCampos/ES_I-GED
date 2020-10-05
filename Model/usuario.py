class Usuario:
    def __init__(self, nome, codigo_identificacao):
        self.nome = nome
        self.codigo_identificacao = codigo_identificacao

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_codigo_identificacao(self):
        return self.codigo_identificacao

    def set_codigo_identificacao(self, codigo_identificacao):
        self.numero_identificacao = codigo_identificacao
