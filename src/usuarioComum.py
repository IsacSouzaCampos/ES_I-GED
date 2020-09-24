from src import usuario


class UsuarioComum(usuario.Usuario):
    def __init__(self, nome=None, numero_identificacao=None):
        super().__init__(nome=nome, numero_identificacao=numero_identificacao)
        self.numero_identificacao = numero_identificacao
