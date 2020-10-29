from Model import usuario


class UsuarioComum(usuario.Usuario):
    def __init__(self, nome=None):
        super().__init__(nome=nome)
