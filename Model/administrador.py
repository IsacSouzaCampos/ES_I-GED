from Model import usuario


class Administrador(usuario.Usuario):
    def __init__(self, nome=None):
        super().__init__(nome=nome)
