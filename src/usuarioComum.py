from src import usuario


class UsuarioComum(usuario.Usuario):
    def __init__(self, numero_identificacao=''):
        self.numero_identificacao = numero_identificacao

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
