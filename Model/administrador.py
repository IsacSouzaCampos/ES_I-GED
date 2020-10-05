from Model import usuario


class Administrador(usuario.Usuario):
    def __init__(self, nome=None, codigo_identificacao=None):
        super().__init__(nome=nome, codigo_identificacao=codigo_identificacao)
        self.codigo_identificacao = codigo_identificacao
